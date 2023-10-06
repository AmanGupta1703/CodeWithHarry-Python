"""
- # Set the value of variable 'a' to 17
- This comment explains that the code is assigning the value of 17 to the variable 'a'. It is a simple statement that sets the initial value of the variable.
"""

#? What is a variable?
#* A variable is a named storage location that holds a value. It acts as a container for storing data that can be accessed and manipulated throughout the program. 

#? What is a data type?
#* Data types represent the kind of value that a variable can hold. 

a = 17;     # Integer
b = True;   # Boolean
c = "Aman"; # String
d = None;   # NoneType
print(a);

# Getting the type of the variable
print("Type of a is", type(a));
print("Type of b is", type(b));
print("Type of c is", type(c));
print("Type of d is", type(d));

"""
# Output:
    - Type of a is <class 'int'>
    - Type of b is <class 'bool'>
    - Type of c is <class 'str'>
    - Type of d is <class 'NoneType'>
"""

#? Creating a complex number
#? Define Complex Number
#* A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers, and i is a solution of the equation x2 = −1.
complexNumber = complex(2, 3);
print("Complex number is", complexNumber);

"""
#  Output:
    - Complex number is (2+3j)
"""

#? Define list
#* A list in Python is a collection of objects which are ordered and mutable.
#? Creating a list
list = [1, 2, 3, 4, 5];
print("List is", list);

""" 
# Output:
    - List is [1, 2, 3, 4, 5]
"""

#? Define tuple
#* A tuple in Python is a collection of objects which are ordered and immutable.
#? Creating a tuple
tuple = (1, 2, 3, 4, 5);
print("Tuple is", tuple);

"""
# Output:
    - Tuple is (1, 2, 3, 4, 5)
"""

#? Define Dictionary
#* A dictionary in Python is a collection of objects which are unordered, mutable and indexed.
#? Creating a dictionary
dictionary = {1: "Aman", 2: "Kumar", 3: "Singh"};
print("Dictionary is", dictionary); 