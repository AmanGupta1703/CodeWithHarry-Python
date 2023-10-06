
#* Python Input and Output

#! Getting Input from User
name = input("Enter your name: ");  #? input() function is used to get input from user
print("Hello " + name + "!");  #? Printing the name of the user

#! input() function always returns a string value even 
#! if the user enters a number or any other data type 
#! value as input

num1 = input("Enter first number: ");
num2 = input("Enter second number: ");

#? To add two numbers, we need to convert the string values to integer values. 
#? We can do this by using int() function.

#! If we don't convert the string values to integer values,
#! then the two numbers will be concatenated instead of addition.

add = int(num1) + int(num2);
print("Result:", str(add));

#! We can also use float() function to convert the string values to float values.

"""
# Output:
    - Enter your name: John
    - Hello John!

    - Enter first number: 10
    - Enter second number: 20
    - Result: 30
"""

