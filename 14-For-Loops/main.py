
#? What is For Loop?
#* For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#? String Example:

print("String Example: ");
name = "Aman";
for character in name: #* Here, character is a variable that will store the value of each character in name.
    print(character, end=", "); #* end=", " is used to print the output in a single line. 

#? Output: A, m, a, n,

print("\n\nList Example: ");

#? List Example:
colors = ["red", "green", "blue", "purple", "indigo"];

for color in colors: #* Here, color is a variable that will store the value of each color in colors.
    print(color, end=", ") 
    for character in color:
        print(character, end=", ");
    print();

#? Output: red, r, e, d, green, g, r, e, e, n, blue, b, l, u, e, purple, p, u, r, p, l, e, indigo, i, n, d, i, g, o, 

#? range() function:
#* Will start from 0 and end at 19.
for num in range(5):
    print(num); #? Output: 0, 1, 2, 3, 4

#* Will start from 1 and end at 8.
for num in range(1, 9):
    print(num); #? Output: 1, 2, 3, 4, 5, 6, 7, 8

print()
for num in range(1, 9, 2): #* 2 is the step value.
    print(num); #? Output: 1, 3, 5, 7

#? What is step value?
#* Step value is the value by which the loop will increment.


"""
    - DONE FOR TODAY -
"""