#from __future__ import print_function
from PIL import Image
#import Image

assemblyMode = ":assemble:complex"

functions = ["nop", "push", "pop", "add", "sub", "jump", "condjump", "ret",
                    "condkill", "transform", "inp", "dup", "mul", "emptykill",
                 "reverse", "rot", "over", "swap", "drop", "inpint", "waitfor",
                 "singlekill", "runifonly"]

'''
Read text file and return content as a list of lines containing lists of
tokens
'''
def readFileContent(fileName):
    global assemblyMode
    # Read in the assembly mode
    assemblyModeCheck = open(fileName).readline().rstrip().lower()
    if (assemblyModeCheck == ":assemble:simple"):
        assemblyMode = ":assemble:simple"



    lines = []
    file = open(fileName, "r")
    # Read line by line
    for line in file:
        # Remove start whitespace and lines starting with REM (remarks)
        if( line.lstrip()[:3] != "rem" and len(line.lstrip()) > 1 and line.lstrip()[0] != ":"):
            # Split remaining lines into tokens (add these to tokens list)
            lines.append(line.split())
    # Return tokens
    return lines


# Write the code to the image
def writeCompiledImg(inputImgName, outputImgName, lines):
    # Use the PIL Image library to open the input image
    im = Image.open(inputImgName)
    pix = im.load()

    # Variables used by :assemble:simple
    imageWidth, imageHeight = im.size
    nextX, nextY = 0, 0
    flagDir = 0 # east

    # Get the number of tokens
    numberLines = len(lines)

    # For the number of tokens
    for index in range(numberLines):
        if (assemblyMode == ":assemble:complex"):
            x, y, r, g, b = pixFromLineComplex(lines[index])
        if (assemblyMode == ":assemble:simple"):
            nextX, nextY, flagDir, x, y, r, g, b = pixFromLineSimple(lines[index],
                                                            nextX, nextY, imageWidth,
                                                                     flagDir)

        #print (x, y, r, g, b)
        pix[int(x), int(y)] = (int(r), int(g), int(b))

    # Save the compiled image
    im.save(outputImgName, quality = 95)

    return 0


def pixFromLineComplex(line):

    # Operates on a stack
    #functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub,
    #             5: jump, 6: condjump, 7: ret, 8: condkill,
    #             9: transform, 10: inp, 11: dup, 12: mul,
    #             13: emptykill, 14: reverse, 15: rot, 16: over,
    #             17: swap, 18: drop, 19: inpint, 20: waitfor,
    #             21: singlekill, 22:runifonly}
    # 1111 = WSEN

    '''
    Syntax should be in the form: x y func data exit_dir
    eg 0 0 push 32 s&e (pix[0,0] = (1, 32, 6) - push a space onto the stack
    then load instruction to the south and the east [0,1] and [1,0])
    '''


    x = line[0]
    y = line[1]
    r = 0
    g = line[3]
    b = 0

    # Convert an function to its int
    for function in range (len(functions)):
        if line[2].lower() == functions[function]:
            r = function

    # If data contains : then convert char to ord
    if line[3][0] == ":":
        g = ord(line[3][1])

    # Convert a direction(s) to its int
    direction = line[4].lower()
    for char in direction:
        if 'w' == char:
            b = b | 8
        if 's' == char:
            b = b | 4
        if 'e' == char:
            b = b | 2
        if 'n' == char:
            b = b | 1

    return x, y, r, g, b

def pixFromLineSimple(line, nextX, nextY, imageWidth, flagDir):

    # Operates on a stack
    #functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub,
    #             5: jump, 6: condjump, 7: ret, 8: condkill,
    #             9: transform, 10: inp, 11: dup, 12: mul,
    #             13: emptykill, 14: reverse, 15: rot, 16: over,
    #             17: swap, 18: drop, 19: inpint, 20: waitfor,
    #             21: singlekill, 22:runifonly}
    # 1111 = WSEN
    # Additional function end

    '''
    Syntax should be in the form: func data
    eg push 32 push a space onto the stack
    then load the next instruction)
    '''


    x = nextX
    y = nextY
    r = 0
    g = line[1]
    b = 0

    isEnd = False

    if line[0] == 'end':
        r = 0
        isEnd = True

    # Convert an function to its int
    for function in functions:
        if line[0].lower() == function:
            r = function

    # If data contains : then convert char to ord
    if line[1][0] == ":":
        g = ord(line[1][1])


    if (not isEnd):
        if (flagDir == 0):
            if(x < imageWidth):
                b = 2 # east
                nextX = x + 1
            else:
                b = 4 # south
                nextY = y + 1
                flagDir = 1
        if (flagDir == 1):
            if (x > 0):
                b = 8 # west
                nextX = x - 1
            else:
                b = 4 # south
                nextY = y + 1
                flagDir = 0
    else:
        b = 0

    return nextX, nextY, flagDir, x, y, r, g, b




def cli():
    print("Assemble or Quit? " +
          "(A, q)" )
    choice = input(">")[0].lower()

    # Quit application
    if choice == "q":
        return True

    # Assemble
    print("Type in the path to the code file")
    codeFile = input(">")
    print("Type in the path to the output image")
    outputImgName = input(">")

    lines = readFileContent(codeFile)
    writeCompiledImg("blank.png", outputImgName, lines)


# Run the CLI while the user has not finished
finished = False
while not finished:
    finished = cli()


