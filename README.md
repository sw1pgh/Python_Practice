# Python_Practice
This Repository contains all the codes that I will be learning and writing while learning python simultaneously. Along with this, it will also be containing any projects that I believe would make sense doing.  
<br />

> Install modules using:
- pip install -r requirements.txt [Windows]  
or
- pip3 install -r requirements.txt [Mac]  
<br />

> Module: A module is a file containing code written by someone else(usually) which can be imported and used in our programs  
<br />

> pip/pip3: It is the package manager for python. You can use pip/pip3 to install a module on your system  
<br />

> Types of Modules:
- Built in Modules [Pre-installed in Python]
- External Modules [Need to be installed using pip/pip3]  
<br />

> REPL = Read Evaluate Print Loop 
- Simply go to the terminal and type python/python3, it will open REPL to code  
<br />

-> # Single Line Comment

-> ''' Multi Line Comment'''  
<br />

> ERROR1: The error you're encountering suggests that Python is trying to use your script file named requests.py instead of the actual requests library. When you name your script the same as a module, it can lead to conflicts.

> A variable is a name given to a memory location in a program.
- variables: container to store a value
- keywords: reserved words in python and cannot be used to name a variable
- identifiers: class/function/variable name  
<br />  

> Types of Data Types in Python:
- Integers
- Floating Point Numbers
- String
- Boolean
- None  
<br />

> Python is a fantastic language that automatically identifies the tyoe of data for us.  

> Rules of defining a variable name(also applies to other identifiers)
- A variable name CAN contain alphabets, digits and underscores
- A variable name CAN only start with an alphabet or underscore
- A variable name CANNOT start with a digit
- No white space is allowed to be used inside a variable name:
- Eg.: my_name, isNegative, integer_1, _integer2  
<br />  

> Operators in Python:
- Arithmetic Operators: +,-,*,/ etc.
- Assignment Operators: =,+=,-=, etc.
- Comparison operators: ==,>,>=,<,!= etc.
- Logical Operators: and, or, not.  

<img src="Images/Log_Op_Logic.png" alt="Logical Operators Logic" style="height: 300px; width:550px;"/><br />

> TYPE() function and TYPECASTING
- type() function is used to find the data type of a given variable in python
- A number can be converted into a string and vice_versa(if possible)
- There are many functions to convert one data type into another  
<br />

> INPUT() function:
- This function allows the user to take input from the keyboard as a string
- It is important to note that the output of input is always a string(even if integer or floating point number is entered)  
<br />

> STRINGS:
- String is a data type in Python
- String is a sequence of characters enclosed in quotes
- Python strings are "immutable" which means they cannot be changed after they are created (Java strings also use this immutable style). Since strings can't be changed, we construct *new* strings as we go to represent computed values.
- We can primarily write a string in three(3) ways:
    - Single quoted string
    - Double quoted string
    - Triple quoted string

<br />   

> String Slicing: 
- A String in Python can be sliced for getting part of strings
- For eg.: name = "Swap" => Length=4 | Index = [0 1 2 3]
- The index in a string starts from 0 ends at (length - 1) in Python.
- In order to slice a string, we can use the following syntax:  

<img src="Images/String_Slicing_Syntax.png" alt="Logical Operators Logic" style="height: 150px; width:550px;"/><br />  

