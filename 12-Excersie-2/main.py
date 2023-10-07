
#? Solution for Excersie 2

#* Write a program that greets the user based on the current time.

import time;

current_hour = time.localtime().tm_hour;

greet = "";

if current_hour >= 6 and current_hour <= 12:
    greet = "Good Morning! ☀️";
elif current_hour >= 12 and current_hour <= 18:
    greet = "Good Afternoon! 🕑";
elif current_hour >= 18 and current_hour <= 22:
    greet = "Good Evening! 🌆";
elif current_hour >= 22 and current_hour <= 6:
    greet = "Good Night! 🌃";

print(greet);

#? Explanation  
#* - We import the time module to get the current time.
#* - We get the current hour using the localtime() function.
#* - We check the current hour using if statements.
#* - We print the appropriate greeting message.
#* - We use the >= and <= operators to check if the current hour is within a certain range.
#* - We use the and operator to check if the current hour is within two ranges.
#* - We use the elif keyword to check for multiple conditions.
#* - We use the else keyword to check for all other conditions.
#* - We use the print() function to print the greeting message. 