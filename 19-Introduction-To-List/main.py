
#? Introduction To List

#* List is a collection of items in a particular order
#* List is mutable
#* List is defined by square brackets []

#? Creating a list

#        0  1  2  3  4
marks = [1, 2, 3, 5, 6];

#? Getting an item from a list.
print(marks[0]); # 1

# Negative Indexing
print(marks[-3]); # 3 (marks[len(marks) - 3]) = marks[5 - 3] = marks[2]

#? Checking if an item is in a list
if 1 in marks:
    print("Yes.");
else:
    print("No.");

if "6" in marks:
    print("Yes.");
else:
    print("No."); 
# ? Output `No`. Since `6` is present in the list but not as a string.(str) but as a number.(int).

#? Same things applies to strings.
if "man" in "Aman":
    print("Yes");

# Slicing but in List
print(marks);
print(marks[:]);
# Both of the above statements will print the same thing.i.e the entire list will be printed.

print(marks[1:4]); #? [2, 3, 5]

# Jump indexing
print(marks[1:4:2]); #? [2, 5]

# List Comprehension
#* List Comprehension is a way to create a list using a for loop.
#* List Comprehension is faster than for loop.

#* Syntax
#* [<expression> for <item> in <list>]

#* Example
#* [i for i in range(10)] will create a list of numbers from 0 to 9.

numbers = [i * i for i in range(1, 10) if i % 2 == 0]
print(numbers);  #? [4, 16, 36, 64]

cubes = [i ** 3 for i in range(1, 10) if i % 3 == 0]
print(cubes); #? [27, 216, 729]