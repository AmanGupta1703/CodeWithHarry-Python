
#! TypeCasting

#? Define Typecasting
#* Typecasting is the process of converting one data type to another data type.

#? Types of Typecasting
#! 1. Implicit Typecasting
#! 2. Explicit Typecasting

#* Implicit Typecasting
#* In this type of typecasting, Python automatically converts one data type to another data type.

#* Explicit Typecasting
#* In this type of typecasting, Python does not convert one data type to another data type automatically.
#* We need to convert it manually.

#? Implicit Typecasting
#* Example
a = 10;
b = 20.5;
c = a + b;

print("The value of c is", c, "and the type of c is", type(c));

"""
# Ouput:
    - The value of c is 30.5 and the type of c is <class 'float'> 
"""

#? Explicit Typecasting
#* Example
a = 10;
b = 20.5;
c = a + int(b);

print("The value of c is", c, "and the type of c is", type(c));
    
""" 
# Ouput:
    - The value of c is 30 and the type of c is <class 'int'> 
"""

