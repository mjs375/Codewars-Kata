# P Y T H O N  •  B A S I C S 
## TUTORIAL
- Indentation matters in Python: it indicates a discrete block of code, such as what is contained in an ```if x>1:``` statement, what is inside a ```function(a)```, a for loop, &c. Once out of the block, de-dent back.

### PYTHON COMMENTS
- Any code after a ```#comment...``` will not be read by the interpreter
- Any code in-between ```"""comment..."""``` will be read as a string literal, but since it isn't assigned to a variable it will simply be ignored.

## STRINGS (DATA STRUCTURE)
- *Strings are immutable, so to 'update a string' you must assign the string to a new one with the changes.*
  - ```string_name = "Some message"``` : *Strings can be in ".." or '..'*
  - ```multiline_string = """Some message,```  
  ```continued on another line,```  
  ```continued on a third line."""```
  - ```string2 = string1 + "some text" + ...``` : *concatenating strings*
  
- **Slice Notation**
  - 
- **f-strings**: *a way to include variables in strings. You can put any valid Python expression inside the {...} to evaluate at runtime.*
  - ```print(f"Hello, {name}.")``` ==> *Hello, David.*
  - ```return f"{name.lower()}"``` ==> *david*
  - ```f"Cost: {apples * 2.99}."```
  - ```print(f"{user[name]} is a {user[job]}.")``` ==> *David is a professor.*
  - ```print(f'{value:.2f}')``` ==> *3.23 (choose decimal place to round at)*

## LISTS (DATA STRUCTURE)
- *Lists are mutable, so you can change them without assigning them to a new list variable. Lists are ordered.*
  - ```list_name.append(value)``` : *adds the value (string, int, another list) to the end of the list. (Note you don't have to set it ```=``` to a new list, as the old list can be updated, being mutable.)*
  - ```for index, value in enumerate(list_name):``` : *loop thru a list, getting additional access to an index-number*



## DICTIONARIES
- *Dicts are mutable and unordered.*
  - ```dict_name = {}``` OR ```dict_name = dict()``` : *create an empty dict. You can also pre-populate the dict with {key:"value", key:"value"} pairs.*
  - ```dict_name[key] = value``` : *set a key/value pair, or update value of existing key*
  - ```print(dict_name.get(key))``` : *get dict value by key*
  - ```del dict_name(key)``` : *delete a dict key/pair*
  - ```for item in dict_name.items():``` : *loop thru dictionary, each 'item' is a (key,value) tuple*
  - ```for key, value in dict_name.items():``` : *Loop thru a dict, having access to key/value individually.*

## SETS
## TUPLES

## STRING SLICE NOTATION:
- **slice(start, stop, step)**: *Start & step are optional. The 'stop' means 'stop 1 before here' (non-inclusive). Step by -1 to reverse a string. Examples of s1="Hello"*
  - ```print(s1[::-1]``` ==> *olleH*
  - ```return s1[::2]``` ==> *Hlo*
  - ```s1[-1:]``` ==> *o*
  


## FUNCTIONS
- def function_name(parameters): *a defined function says what will happen once it is atually called*
- a = fuction_name(parameter): *a function whose return value is outputted as 'a'*
   - ```a,b = function_name(parameters)```: *a function with multiple returns, outputted to 'a,b' in the same order. (Multiple outputs can be stored in 1 variable, but that it must be indexed to get out individual results.)*
- ```a, b = function(a)``` : *here function(a) returns (unseen) two variables. You can also return 2 variables to a single one, but then need to unpack/index it to access them.*

## CLASSES

## OPERATORS
- **Assignment Operators**
  - ```a = 10``` *the __Assignment Operator__. 'Declares' a variable's value (often a new variable).*
  - ```a += 10``` => ```a = a + 10``` *add a thing to itself ('updates' or refurbishes a variable)*
    - *See also:* ```-= , *= , /=, %=, //=, **= ``` *and more...*
- **Arithmetic Operators**
  - ```+, -, *, /, %, **, //```: *addition, subtraction, multiplication, division, modolus (divide and return the remainder), exponentiation, floor division (divide and return number w/0 the remainder).*
- **Comparison Operators**
  - ```x == y```: *checks for equality between the two– if x=10 and y=10, True.*
    - ```x != y```: *checks for non-equality between the variables– if x=10 and y=10, False.*
  - ```x > y, x >= y, x < y, x <= y```: *x is greater than/greater than or equal to y, less than/less than or equal to.*
- **Logical Operators**
  - ```if x < 5 and x < 10```: *joins conditional statements– returns True if both/all statements are True.*
  - ```if x <5 or x > 10```: *returns True if just one of the statements is True.*
  - ```if not (x<5 and x<10)```: reverses the result– returns False if True, True if False.

## DECLARING VARIABLES
  - Variables do not need explicit declarations of type, Python will interpret for you.
- **Multiple Assignment**:
  - ```a = b = c = 10```: *multiple variables given the same single value*
  - ```a,b,c=1,2,"jen"```: *multiple variables given multiple objects, just on the same line*
- **Var: String**
  - ```name = "Cassady"```: 
- **Var: Number**
  - **Integer**
    - ```counter = 1```
  - **Float**: *a float allows for decimal places*
  - ```miles = 100.05```
- **Var: Boolean**
  - ```switch = True```: *when declaring the value of a boolean variable, they must be capitalized (True/False).*
  - Boolean Rules: *any value that exists and returns a non-zero(+ or -) or non-empty value is True; 0 returns False. (Thus some variables, like strings, always return True as long as they aren't empty.)*



## USEFUL FUNCTIONS:
- **enumerate()**: *attaches an iterator (counter) to an object*
  -```for index, value in enumerate(list/string):

