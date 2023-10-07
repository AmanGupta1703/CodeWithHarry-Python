
#? String Slicing
#* [start:stop:step]

#? start: where to start the slice
#? stop: where to end the slice (exclusive)
#? step: the size of the jump to make

#? Why is string slicing useful?
#* String slicing allows us to make substrings from larger strings

#? What is the default start, stop, and step?
#* start = 0
#* stop = length of string
#* step = 1

#? What is the syntax for string slicing?
#* [start:stop:step]

#! It will not include the stop index

# Example 1
#* [start:stop:step]

name = "Aman Gupta";

print(name[0:4]); #* Aman

# Few more examples
print(name[0:]); #* Aman Gupta
# It will start from the 0th index and will go till the 4th index
print(name[:4]); #* Aman

# Automatically takes the length of the string  
print(name[:]); #* Aman Gupta

# Getting the length of the string
print(len(name)); #* 10 

#! It will also include the space in the string. 

# Negative Indexing
print(name[0:-1]); #* Aman Gupt
print(name[0:-4]); #* Aman 

#? If we want to print the last character of the string
print(name[-1]); #! a

#? When we use negative indexing, it will take the length of the string 
#? and then it will subtract the number from the length of the string
print(name[-3:-1]); #* pt

#? Looping through the string
for character in name:
    print(character);

# Quik Quiz
name = "Harry";
print(name[-4:-2]); #* ar

"""
    # Output:
        - Aman
        - 10
        - Aman Gupta
        - Aman
        - Aman Gupta
        - 10
        - Aman Gupt
        - Aman
        - a
        - pt
        - Lopping through the string
        - ar
"""