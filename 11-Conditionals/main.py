
#? What is Conditional Statements?
#* Conditional statements are used to control the flow of our program. They are used to execute certain parts of our code based on conditions that we may set.

#? What are the types of Conditional Statements?
#* if
#* elif
#* else

#? What is the syntax of if statement?  
#* if condition:
#*     statement

#? What is the syntax of if-else statement?
#* if condition:
#*     statement
#* else:
#*     statement

#? What is the syntax of if-elif-else statement?
#* if condition:
#*     statement
#* elif condition:
#*     statement
#* else:
#*     statement

#? What is the syntax of nested if statement?
#* if condition:
#*     if condition:
#*         statement
#*     else:
#*         statement
#* else:
#*     statement

#* Example 1
age = int(input("Enter your age: "));

if age >= 18:
    print("You're eligible to vote.");
else:
    print("You're not eligible to vote.");

#? Explanation
#* - In the above example, we have used the if-else statement to check whether the age is greater than or equal to 18.
#* - If the age is greater than or equal to 18, then the first condition is executed and the program terminates.
#* - If the age is less than 18, then the second condition is executed and the program terminates.

#* Example 2
num = int(input("Enter a number: "));
if num > 0:
    print("The number is positive.");
elif num < 0:
    print("The number is negative.");
else:
    print("The number is zero.");

#? Explanation
#* - In the above example, we have used the if-elif-else statement to check whether the number is positive, negative or zero.
#* - If the number is greater than zero, then the first condition is executed and the program terminates.
#* - If the number is less than zero, then the second condition is executed and the program terminates.
#* - If the number is equal to zero, then the third condition is executed and the program terminates. 

#* Nested if-elif-else statement    
num = int(input("Enter a number: "));
if num >= 0:
    if num == 0:
        print("The number is zero.");
    elif num > 0:
        if (num % 2) == 0:
            print("The number is positive and even.");
        else:
            print("The number is positive and odd.");
    else:
        print("The number is negative.");           


"""
    # What is indentation?
        - Indentation refers to the spaces at the beginning of a code line.
        - Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
        - Python uses indentation to indicate a block of code.
        - Python will give you an error if you skip the indentation.
"""