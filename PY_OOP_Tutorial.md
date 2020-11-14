# Object-Oriented Programming (OOP)

### Programming Paradigms
- **Object-Oriented:** *structuring of programs so that properties and behaviors are bundled into individual __objects__. Objects are the center of OOP, not just in representing data, but the overall structure of the program.*
  - **Object:** *represents an entity with __properties__, e.g. a Person with a Name, Age, Address, and __behaviors__ (like walking, speaking); or an Email, with properties such as a Recipient List, Subject, Body, and behaviors like adding attachments and ending.*
- **Procedural/Functional:** *structures a program like a recipe, i.e. a series of steps in the form of functions and code blocks, which flow sequentially to complete a task.*


### Classes
- **Primitive Data Structures**: *represent simple pieces of information, e.g. strings, integers, lists.*
  - **Example List:** ```kirk, spock  = ["James Kirk", 34, "Captain", 2256], ["Spock", 35, 2254]
    - **Flaws:** *difficult to manage, remembering just what kirk[#] exactly is, errors if all employees don't have the same number of elements in a list...*
- **Classes:** *used to create user-defined data structures.*
  - **Methods:** *class-defined functions, which ID behaviors and actions that an object can perform with its data.*
  - **Class vs. Instance:** *the Class is the blueprint, the 'idea' of a dog (that a Dog has a name, age, breed); an Instance is one actual Dog (Spot, age 3, dalmatian).*

#### Defining a Class
- **Properties:** ```.__init__()``` *method defines all properties that an object of its class must have. Everytime an Object of a Class is initialized, ```.__init__()``` sets initial states for the object by assigning values (any number of parameters, but the first is always ```self```, which helps define attributes on itself).*
- **Instance Attributes:** *created in ```.__init__()```, and are particular to each particular object instance (one dog is named Spot, another Grover).*
- **Class Attributes:** *attributes that have the same value for all instances of the class. Define them by assigning a value to a variable outside of ```.__init__()``` (below the class definition). They must always have an initial value, as all instances of the class are automatically assigned these values.*

```python
class PetDog: # name classes in this way: class ClassName
  species = "Canis familiaris" # class attribute
  def __init__(self, name, age): # method, creating attributes
    self.name = name # creates 'name' attribute, assigns it to the value of the 'name' parameter
    self.age = age # instance attribute
```




[Source](https://realpython.com/python3-object-oriented-programming/)