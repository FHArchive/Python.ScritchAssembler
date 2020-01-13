<p float="left">
<img src="https://img.shields.io/github/languages/top/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="Github top language">
<img src="https://img.shields.io/codacy/grade/:codacy-proj-id:.svg?style=flat-square" alt="Codacy grade">
<img src="https://img.shields.io/codacy/coverage/:codacy-proj-id:.svg?style=flat-square" alt="Codacy coverage">
<img src="https://img.shields.io/github/repo-size/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="Repository size">
<img src="https://img.shields.io/github/issues/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="Issues">
<img src="https://img.shields.io/github/license/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="License">
<img src="https://img.shields.io/github/commit-activity/m/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="Commit activity">
<img src="https://img.shields.io/github/last-commit/fredhappyface/Python.ScritchAssembler.svg?style=flat-square" alt="Last commit">
</p>

# Python.ScritchAssembler

<img src="readme-assets/icons/proj-icon.png" alt="Project Icon" width="100">

This program assembles assembly-like instructions into Stritch programs 
(these are .png files). In the words of roo2319, "Scritch is an esoteric, 
stack-based programming language". See the Scritch project here:
<https://github.com/roo2319/Scritch>

## Download
### Clone
#### Using The Command Line 
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/[user-name]/[repository]
```

More information can be found at 
<https://help.github.com/en/articles/cloning-a-repository> 

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at 
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location


## Language information 
### Built for
This program has been written for Python 3 and has been tested with 
Python version 3.7.0 <https://www.python.org/downloads/release/python-370/> 
on a Windows 10 PC. 
### Other versions
To install Python, go to <https://www.python.org/> and download the latest 
version. 
## How to run
1. Open the .py file in IDLE
2. Run by pressing F5 or by selecting Run> Run Module



## Syntax and instructions

### Code files and execution
- Source code files are best saved as text files (.txt) 
- Source code is assembled into 'object code', these are PNGs (.png)
- The images are then processed by the executor 

### Operand types
#### Int (8 bits)
The minimum value is 0 and the maximum is 255. This is written to the green 
component of the pixel 
#### Char (8 bits) 
These are declared with a ':' and immediately follow. For example the character 
'H' would be ':H'.  This is converted to its ASCII equivalent and is written to 
the green component of the pixel 


### Instructions 
|Instruction     |Description                                                                                                                                                                                                                                                                                                                  |Value|
|:-              |:-                                                                                                                                                                                                                                                                                                                           |-:   |
|```:```         |Special annotation. Can be used to comment, declare the assembler to use (on the first line only), or to use a char as an operand                                                                                                                                                                                            |N/A  |
|```rem```       |```//``` (Java) <br>```#``` (Python)                                                                                                                                                                                                                                                                                         |N/A  |
|```nop```       |No operation (ignores operand)                                                                                                                                                                                                                                                                                               |0    |
|```push```      |Pushes operand to the stack                                                                                                                                                                                                                                                                                                  |1    |
|```pop```       |Pops and prints the first element of the stack, Prints as ascii char if non-zero operand                                                                                                                                                                                                                                     |2    |
|```add```       |Adds top elements of stack unless given non zero arg, otherwise adds top element and the operand. Pushes the result to the stack                                                                                                                                                                                             |3    |
|```sub```       |Subtracts second element from the top element of stack unless given non zero arg, otherwise subtracts operand from the top element. Pushes the result to the stack                                                                                                                                                           |4    |
|```jump```      |Unconditional jump to (stack[0],stack[1]), destroys top 2 elements of stack. Possible to implement in :assemble:simple but difficult as you would have to work out the coordinates yourself (for instructions < image width, jump to (instruction - zero indexed, 0)). Better suited for :assemble:complex. (ignores operand)|5    |
|```condjump```  |Jumps if stack.pop() == operand, destroys top 3 elements of stack                                                                                                                                                                                                                                                            |6    |
|```ret```       |Functions like getpointers, But takes operand as B and top of call stack as location.                                                                                                                                                                                                                                        |7    |
|```condkill```  |Kills pointer if stack.pop() == operand, Destroys top of stack                                                                                                                                                                                                                                                               |8    |
|```transform``` |Transforms current coordinates to have opcode = operand and operand = stack.pop()                                                                                                                                                                                                                                            |9    |
|```inp```       |Reads input as an ASCII char from user and pushes to stack. (ignores operand)                                                                                                                                                                                                                                                |10   |
|```dup```       |Duplicates top element of stack. Assuming that the stack contains (top) [5, 2, 3],  duplicate the value 5 - so the stack becomes (top) [5, 5, 2, 3] (ignores operand)                                                                                                                                                        |11   |
|```mul```       |Multiplies top elements of stack unless given a non-zero operand. Otherwise multiplies top of the stack and the operand                                                                                                                                                                                                      |12   |
|```emptykill``` |Removes outgoing pointers if the stack is empty. Assuming the stack has contents, does nothing (ignores operand)                                                                                                                                                                                                             |13   |
|```reverse```   |Reverses the stack. Reverses the stack. Assuming that the stack contains (top) [5, 2, 3], the stack becomes (top) [3, 2, 5] (ignores operand)                                                                                                                                                                                |14   |
|```rot```       |Rotates stack such that <br>n1     n3<br>n2  -> n1<br>n3     n2. <br>Assuming that the stack contains (top) [5, 2, 3, 4, 5], the stack becomes (top) [3, 5, 2, 4, 5] (ignores operand)                                                                                                                                       |15   |
|```over```      |Makes a copy of the second item and pushes it to the top. Assuming that the stack contains (top) [5, 2, 3], the stack becomes (top) [2, 5, 2, 3] (ignores operand)                                                                                                                                                           |16   |
|```swap```      |Swaps the top two elements of the stack. Assuming that the stack contains (top) [5, 2, 3], the stack becomes (top) [2, 5, 3] (ignores operand)                                                                                                                                                                               |17   |
|```drop```      |Removes the top of the stack. Assuming that the stack contains (top) [5, 2, 3], the stack becomes (top) [2, 3] (ignores operand)                                                                                                                                                                                             |18   |
|```inpint```    |Reads input from user as an integer and pushes to stack. (ignores operand)                                                                                                                                                                                                                                                   |19   |
|```waitfor```   |Waits for stack to equal operand before proceeding                                                                                                                                                                                                                                                                           |20   |
|```singlekill```|Kills if stack has one element. (ignores operand)                                                                                                                                                                                                                                                                            |21   |
|```runifonly``` |Runs if it is the last pointer. (ignores operand)                                                                                                                                                                                                                                                                            |22   |



### :assemble:simple
General considerations:
- :assemble:simple is the easiest way to program in Scritch source but is also 
the least powerful

- Only one instruction can be loaded after another 

- 'end' must be used to declare the end of the file 

- each non-commented or annotated line must be in the form 'opcode operand' 

- Operands must be as described above (an int 0-255 or a char, declared with 
a ':')

|Instruction     |Example                    |Comments                                                                                                                                 |
|:-              |:-                         |:-                                                                                                                                       |
|```:```         |```:assemble:simple```     |Tells the compiler that the program has been written in the simple form and to generate pixels and the exit direction                    |
|```rem```       |```rem This is a comment```|                                                                                                                                         |
|```nop```       |```nop 0```                |As nop is no operation, nothing will happen. 'end' leverages this command. This is more useful for :assemble:complex (ignores operand)   |
|```push```      |```push :H```              |Pushes the ASCII character 'H' to the stack                                                                                              |
|```pop```       |```pop 1```                |Will print the top element of the stack as an ASCII character. Following ```push :H``` it would print 'H'                                |
|```add```       |```add 0```                |Adds the two top elements                                                                                                                |
|```sub```       |```sub 1```                |Subtracts 1 from the top of the stack                                                                                                    |
|```ret```       |```ret 0```                |                                                                                                                                         |
|```condkill```  |```condkill 5```           |Pops the top value off the stack and compares this to the argument. Assuming the stack holds [5] this command would terminate the program|
|```inp```       |```inp 0```                |                                                                                                                                         |
|```dup```       |```dup 0```                |                                                                                                                                         |
|```mul```       |```mul 22```               |Assuming that the stack contains (top) [5, 2, 3],  multiply the value 5 by 22 and push the result to the stack                           |
|```emptykill``` |```emptykill 0```          |                                                                                                                                         |
|```reverse```   |```reverse 0```            |                                                                                                                                         |
|```rot```       |```rot 0```                |                                                                                                                                         |
|```over```      |```over 0```               |                                                                                                                                         |
|```swap```      |```swap 0```               |                                                                                                                                         |
|```drop```      |```drop 0```               |                                                                                                                                         |
|```inpint```    |```inpint 0```             |                                                                                                                                         |
|```waitfor```   |```waitfor 0```            |                                                                                                                                         |
|```singlekill```|```singlekill 0```         |                                                                                                                                         |
|```runifonly``` |```runifonly 0```          |                                                                                                                                         |
|```end```       |```end 0```                |Leverages nop and sets blue to 0 (no pointer) this terminates the program                                                                |


#### More complex programs in :assemble:simple
Instructions that require the programmer to have knowledge of how the compiler constructs the image. 

- Written to the image such that if there where 12 instructions and each 
instruction was numbered from 1 to 12, and the image had a width of 4:

|   |   |   |   |
|:-:|:-:|:-:|:-:|
|1  |2  |3  |4  |
|8  |7  |6  |5  |
|9  |10 |11 |12 |


|Instruction    |Example           |Comments                                                                                                                                                                                   |
|:-             |:-                |:-                                                                                                                                                                                         |
|```jump```     |```jump 0```      |Assuming the stack contents are (top) [5,0], jump to the 6th instruction (stored in pixel 5,0). Destroys the top two values (ignores operand)                                              |
|```condjump``` |```condjump 6```  |Assuming the stack contents are (top) [6,5,0], jump to the 6th instruction (stored in pixel 5,0) as the operand (6) equals the top element of the stack (6). Destroys the top 3 values     |
|```transform```|```transform 12```|Assuming that the stack contains (top) [5, 2, 3]. Change the current instruction to mult 5. If the pixel is revisited through a jump, then the instruction would be mult 5 in this instance|



### :assemble:complex
A note on exit direction:
- Next instructions are loaded in the order North, East, South, West
for example, if n&s is specified then the instruction at position (x, y-1)
is loaded next, followed by the instruction at position (x, y+1)

- & are ignored and have been included to improve readability (n&e&s - load 
North, East and South)

- If there is no exit direction, use any character apart from 'nesw' (includes 
uppercase variants). '-' and '0' would make most sense 

General considerations:
- :assemble:complex is the least user-friendly way to program in Scritch 
but makes for easier development of more complex programs (such as those 
using jump - this is possible in :assemble:simple but requires the 
programmer to think about how the instructions will be laid out in the image)

- Up to three instructions can be loaded after another 

- each non-commented or annotated line must be in the form 'x y opcode operand 
exit_direction'

- Operands must be an int 0-255 or a char, declared with a ':'


|Instruction     |Example                    |Comments                                                                                                                                                                                                                                                           |
|:-              |:-                         |:-                                                                                                                                                                                                                                                                 |
|```:```         |```:assemble:complex```    |Tells the compiler that the program has been written in the complex form and that the programmer has decided where each instruction will be stored along with the exit direction                                                                                   |
|```rem```       |```rem This is a comment```|                                                                                                                                                                                                                                                                   |
|```nop```       |```0 0 nop 0 s```          |At pixel 0, 0 and add the instruction to the south to the next instruction stack                                                                                                                                                                                   |
|```push```      |```7 8 push :H e&w```      |Pushes the ASCII character 'H' to the stack. At pixel 7, 8 and add the instruction to the east, and west to the next instruction stack                                                                                                                             |
|```pop```       |```23 5 pop 1 -```         |Will print the top element of the stack as an ASCII character. Following ```push :H``` it would print 'H'. At pixel 23, 5                                                                                                                                          |
|```add```       |```7 9 add 0 -```          |Adds the two top elements. At pixel 7, 9                                                                                                                                                                                                                           |
|```sub```       |```2 0 sub 1 -```          |Subtracts 1 from the top of the stack. At pixel 2, 0                                                                                                                                                                                                               |
|```jump```      |```4 6 jump 0 -```         |Assuming the stack contents are (top) [5,0], jump to the instruction (stored in pixel 5,0). At pixel 4, 6                                                                                                                                                          |
|```condjump```  |```4 9 condjump 6 w```     |Assuming the stack contents are (top) [6,5,0], jump to the instruction (stored in pixel 5,0) as the operand (6) equals the top element of the stack (6). Destroys the top 3 values. At pixel 4, 9 and add the instruction to the west to the next instruction stack|
|```ret```       |```1 3 ret 0 n&e```        |At pixel 1, 3 and add the instruction to the north, and east to the next instruction stack                                                                                                                                                                         |
|```condkill```  |```11 9 condkill 0 e```    |At pixel 11, 9 and add the instruction to the east to the next instruction stack                                                                                                                                                                                   |
|```transform``` |```22 8 transform 12 -```  |Assuming that the stack contains (top) [5, 2, 3]. Change the current instruction to mult 5. If the pixel is revisited through a jump, then the instruction would be mult 5 in this instance. At pixel 22, 8                                                        |
|```inp```       |```2 18 inp 0 e```         |At pixel 2, 18 and add the instruction to the east to the next instruction stack                                                                                                                                                                                   |
|```dup```       |```9 20 dup 0 s&w```       |At pixel 9, 20 and add the instruction to the south, and west to the next instruction stack                                                                                                                                                                        |
|```mul```       |```7 4 mul 0 n&s```        |At pixel 7, 4 and add the instruction to the north, and south to the next instruction stack                                                                                                                                                                        |
|```emptykill``` |```0 9 emptykill 0 e&w```  |At pixel 0, 9 and add the instruction to the east, and west to the next instruction stack                                                                                                                                                                          |
|```reverse```   |```2 5 reverse 0 -```      |At pixel 2, 5                                                                                                                                                                                                                                                      |
|```rot```       |```8 7 rot 0 -```          |At pixel 8, 7                                                                                                                                                                                                                                                      |
|```over```      |```6 5 over 0 w```         |At pixel 6, 5 and add the instruction to the west to the next instruction stack                                                                                                                                                                                    |
|```swap```      |```17 11 swap 0 n```       |At pixel 17, 11 and add the instruction to the north to the next instruction stack                                                                                                                                                                                 |
|```drop```      |```1 3 drop 0 s```         |At pixel 1, 3 and add the instruction to the south to the next instruction stack                                                                                                                                                                                   |
|```inpint```    |```1 1 inpint 0 s```       |At pixel 1, 1 and add the instruction to the south to the next instruction stack                                                                                                                                                                                   |
|```waitfor```   |```2 2 waitfor 0 -```      |At pixel 2, 2                                                                                                                                                                                                                                                      |
|```singlekill```|```6 2 singlekill 0 e```   |At pixel 6, 2 and add the instruction to the east to the next instruction stack                                                                                                                                                                                    |
|```runifonly``` |```1 8 runifonly 0 n&e&s```|At pixel 1, 8 and add the instruction to the north, and east, and south to the next instruction stack                                                                                                                                                              |



### Hello World - Example 

#### :assemble:simple 
|Code         |Comments                                   |
|:-           |:-                                         |
|```push :H```|Push the character 'H' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'H')|
|```push :E```|Push the character 'E' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'E')|
|```push :L```|Push the character 'L' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'L')|
|```push :L```|Push the character 'L' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'L')|
|```push :O```|Push the character 'O' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'O')|
|```push :W```|Push the character 'W' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'W')|
|```push :O```|Push the character 'O' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'O')|
|```push :R```|Push the character 'R' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'R')|
|```push :L```|Push the character 'L' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'L')|
|```push :D```|Push the character 'D' to the stack        |
|```pop 1```  |Pop the stack (print the top element - 'D')|



#### :assemble:complex

##### Code 
|Code                 |Comments                                                         |
|:-                   |:-                                                               |
|```1 3 push :H s```  |Push the character 'H' to the stack, go south                    |
|```2 2 push :E -```  |Push the character 'E' to the stack                              |
|```1 2 push :L e&s```|Push the character 'L' to the stack, go east, then south         |
|```2 1 push :L -```  |Push the character 'L' to the stack                              |
|```0 2 push :O e```  |Push the character 'O' to the stack, go east                     |
|```1 1 push :W e```  |Push the character 'W' to the stack, go east                     |
|```2 0 push :O -```  |Push the character 'O' to the stack                              |
|```0 1 push :R e&s```|Push the character 'R' to the stack, go east, then south         |
|```1 0 push :L e```  |Push the character 'L' to the stack, go east                     |
|```0 0 push :D e&s```|Push the character 'D' to the stack, go east, then south         |
|```1 4 pop 1 e&s&w```|Pop (and print) the character 'H', go east, then south, then west|
|```2 4 pop 1 -```    |Pop (and print) the character 'E'                                |
|```1 5 pop 1 e&s&w```|Pop (and print) the character 'L', go east, then south, then west|
|```0 4 pop 1 -```    |Pop (and print) the character 'L'                                |
|```2 5 pop 1 e&s```  |Pop (and print) the character 'O', go east, then south           |
|```1 6 pop 1 -```    |Pop (and print) the character 'W'                                |
|```0 5 pop 1 s```    |Pop (and print) the character 'O'                                |
|```3 5 pop 1 -```    |Pop (and print) the character 'R'                                |
|```2 6 pop 1 -```    |Pop (and print) the character 'L'                                |
|```0 6 pop 1 -```    |Pop (and print) the character 'D'                                |



##### In Image 
||0|1|2|3|
|:-:|:-:|:-:|:-:|:-:|
|0|push :D ⬇ ➡|push :L ➡|push :O |X|
|1|push :R ⬇ ➡|push :W ➡|push :L |X|
|2|push :O ➡|push :L ⬇ ➡|push :E |X|
|3|X|push :H ⬇ |X|X|
|4| pop 1 |pop 1 ⬅ ⬇ ➡ |pop 1|X|
|5|pop 1 ⬇ |pop 1 ⬅ ⬇ ➡ |pop 1 ⬇ ➡ |pop 1|
|6|pop 1|pop 1|pop 1|X|


##### Navigation 
|Instruction|Next                            |Stack                                                  |
|:-         |:-                              |:-                                                     |
|push :D    |[(1, 0), (0, 1)]                |(top)['D']                                             |
|push :L    |[(0, 1), (2, 0)]                |(top)['L', 'D']                                        |
|push :R    |[(2, 0), (1, 1), (0, 2)]        |(top)['R', 'L', 'D']                                   |
|push :O    |[(1, 1), (0, 2)]                |(top)['O', 'R', 'L', 'D']                              |
|push :W    |[(0, 2), (2, 1)]                |(top)['W', 'O', 'R', 'L', 'D']                         |
|push :O    |[(2, 1), (1, 2)]                |(top)['O', 'W', 'O', 'R', 'L', 'D']                    |
|push :L    |[(1, 2)]                        |(top)['L', 'O', 'W', 'O', 'R', 'L', 'D']               |
|push :L    |[(2, 2), (1, 3)]                |(top)['L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']          |
|push :E    |[(1, 3)]                        |(top)['E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']     |
|push :H    |[(1, 4)]                        |(top)['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']|
|pop 1      |[(2, 4), (1, 5), (0, 4)]        |(top)['E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']     |
|pop 1      |[(1, 5), (0, 4)]                |(top)['L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']          |
|pop 1      |[(0, 4), (2, 5), (1, 6), (0, 5)]|(top)['L', 'O', 'W', 'O', 'R', 'L', 'D']               |
|pop 1      |[(2, 5), (1, 6), (0, 5)]        |(top)['O', 'W', 'O', 'R', 'L', 'D']                    |
|pop 1      |[(1, 6), (0, 5), (3, 5), (2, 6)]|(top)['W', 'O', 'R', 'L', 'D']                         |
|pop 1      |[(0, 5), (3, 5), (2, 6)]        |(top)['O', 'R', 'L', 'D']                              |
|pop 1      |[(3, 5), (2, 6), (0, 6)]        |(top)['R', 'L', 'D']                                   |
|pop 1      |[(2, 6), (0, 6)]                |(top)['L', 'D']                                        |
|pop 1      |[(0, 6)]                        |(top)['D']                                             |
|pop 1      |[]                              |(top)[]                                                |



### How are the pixels encoded?
|R     |G      |B             |
|:-:   |:-:    |:-:           |
|OPCODE|OPERAND|EXIT DIRECTION|


The opcode ranges from 0 to 22, the operand 0 to 255 and the exit direction 
is effective at 0 to 15.


### What is exit direction?
Exit direction is the direction that the program flows. Execution starts in 
the top right [0,0] and the B value represents which adjacent pixels should 
be added to the execution queue. It is represented as a one hot encoded value 
such that 1111 represents WSEN. 




## Licence 
MIT License
Copyright (c) fredhappyface
(See the [LICENSE](/LICENSE.md) for more information.)
