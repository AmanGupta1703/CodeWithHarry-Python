
#? What is Match Case Statement?

#* Match Case Statement is a new feature in Python 3.10. 
#* It is used to replace the if-elif-else statement. It is also known as Switch Case Statement. 
#* It is used to compare the value of an expression against multiple values.
#* It is similar to the switch statement in other programming languages like C, C++, Java, etc. 

#* Syntax:

#* match expression:
#*     case value1:
#*         statement
#*     case value2:
#*         statement
#*     case _:
#*         statement

#* Example:
x = int(input("Enter a number: "));

match x:
    case 1:
        print("One");
    case 4:
        print("Two");
    case _ if x != 90:
        print(x, "is not 90");
    case _ if x != 80:
        print(x, "is not 80");
    case _ if x != 70:
        print(x, "is not 70");
    case _:
        print(x);

#? `_` means default case. If no case matches, then default case will be executed.