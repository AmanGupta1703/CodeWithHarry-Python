
#? What are Functions?
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


#? Function with no arguments   
def greet():
    print("Welcome to Functions in Python!");

#? Function with no function body.
def isLower():
    pass;

greet();
print();

#? Creating a Function
def calculateGeometricMean(a, b):
    mean = (a * b) / (a + b);
    print("Mean:", mean);

def isGreater(a,b):
    if (a > b):
        print(a, "is greater than", b);
    else:
        print(a, "is less than or equal to", b);

a = 10;
b = 20;
calculateGeometricMean(a, b);
isGreater(a, b);

c = 30;
d = 10;
calculateGeometricMean(c, d);
isGreater(c, d);


#? Few important built-in functions examples
# - abs()
# - max()
# - min()
# - pow()
# - round()
# - sum()


#? Function Explanation
# - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
# - Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
# - The first statement of a function can be an optional statement - the documentation string of the function or docstring.
# - The code block within every function starts with a colon (:) and is indented.
# - The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

