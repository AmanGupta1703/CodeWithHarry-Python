
#? Types of function arguments?
#* 1. Positional Arguments
#* 2. Keyword Arguments
#* 3. Default Arguments
#* 4. Variable Length Arguments
    #* - *args (Non-Keyword Arguments)
    #* - **kwargs (Keyword Arguments)

#* 1. Positional Arguments => Positional arguments are the arguments passed to the function in correct positional order. The number of arguments in the function call should match exactly with the function definition.
def sum(a, b):
    print(a + b);

sum(5, 6); # 11

#* 2. Keyword Arguments => Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
def sum(a, b):
    print(a + b);

sum(b = 5, a = 6); # 11

#* 3. Default Arguments => A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
def sum(a, b = 5):
    print(a + b);

sum(6); # 11

#* 4. Arbitrary Arguments => Sometimes, you do not know in advance the number of arguments that will be passed into your function. Python allows you to handle this kind of situation through function calls with an arbitrary number of arguments.

def sum(*numbers):
    print(numbers); # (12, 90, 30, 60) => It will be of type tuple.
    sum = 0;
    for number in numbers:
        sum += number;
    print("Sum:", sum, "\nAverage:", sum / len(numbers));

sum(12, 90, 30, 60);

#* 5. Arbitrary Keyword Arguments => Sometimes, you do not know in advance the number of keyword arguments that will be passed into your function. Python allows you to handle this kind of situation through function calls with an arbitrary number of keyword arguments.

#? **kwargs => If you want to handle named arguments in a function, you should use the following syntax:
#? It will of type dictionary.
def fullName(**name):
    print(name); # {'first_name': 'Aman', 'last_name': 'Gupta'} => It will be of type dictionary.
    print("My name is", name["first_name"], name["last_name"] + ".");

fullName(first_name = "Aman", last_name = "Gupta");


#? Return Statement
def sum(a, b):
    return a + b; #! Return statement => It will return the value to the function call.

total = sum(5, 6); #? It will store the value of sum in total variable.
print(total); # 11

