
#? What is `while` loop?
#* `while` loop is a loop that will run until the condition is met.

#? Syntax 
#* while condition:
#*     code


i = 0;
while i < 3:
    print(i); #? Output: 0, 1, 2
    i += 1; 

#? Taking input from the user

# number = int(input("Enter a number: "));
number = 11;

while number < 10:
    number = int(input("Enter a number: "));
    print("You entered: ", number);
print("Breaking out of the loop...");


# Decrement Loop
i = 10; #? Start from 10 
while i > 0: #? Run until 0
    print(i);   #? Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    i -= 1; #? Decrement by 1

#? If i === 0, the interpreter will break out of the loop.

#? Else with while loop
i = 0;
while i < 5:
    print(i); #? Output: 0, 1, 2, 3, 4
    i += 1; 
else:
    print("i is no longer less than 5");


#? D0-While Loop

#* D0-While loop is a loop that will run at least once.

#? Syntax
#* do:
#*     code
#* while condition

while True:
    number = int(input("Enter a positive number: "));
    print(number);
    if not number > 0:
        break



#? what is iteration?
#! Iteration is the process of looping through the items of an iterable object.

#? What is `interpreter`?
#! `interpreter` is a program that reads and executes code. Python is an interpreted language.