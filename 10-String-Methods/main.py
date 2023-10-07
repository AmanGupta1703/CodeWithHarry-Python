
#? String Methods
#* String methods are used to perform operations on strings.

#* String methods are called by using the dot operator (.) on a string object,
#* and can also take parameters, just like a function.

#* The len() function returns the length of a string:

a = "Hello, World!";
print(len(a));

#* The lower() method returns the string in lower case:
print(a.lower()); #? Output: hello, world! 

#* The upper() method returns the string in upper case:
print(a.upper()); #? Output: HELLO, WORLD!

#* The rstrip() method removes any whitespace from the right side:
#! Note: The rstrip() method removes only from the right side.
a = "!!Hello, World. !!!";
print(a.rstrip("!")); #? Output: !!Hello, World.

#* The replace() method replaces a string with another string:
print(a.replace("!", "?")); #? Output: ??Hello, World. ???

#* The split() method splits the string into substrings if it finds instances of the separator:
#!  - If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
print(a.split(",")); #? Output: ['!!Hello', ' World. !!!']

#* The capatalize() method converts the first character to upper case:  
a = "aman gupta";
print(a.capitalize()); #? Output: Aman gupta

#* The center() method will center align the string, using a specified character (space is default) as the fill character.
print(a.center(20)); #? Output:     aman gupta

#* The count() method returns the number of times a specified value appears in the string.
print(a.count("a")); #? Output: 3

#* The endswith() method returns True if the string ends with the specified value, otherwise False.
print(a.endswith("a")); #? Output: True
print(a.endswith("", 0, 4)); #? Output: True

#* The startsWith() method returns True if the string starts with the specified value, otherwise False.
print(a.startswith("a")); #? Output: True

#* The find() method finds the first occurrence of the specified value.
#! Note: The find() method returns -1 if the value is not found.
print(a.find("a")); #? Output: 0
print(a.find("z")); #? Output: -1

#* The index() method finds the first occurrence of the specified value.
#! Note: The index() method raises an exception if the value is not found.
print(a.index("a")); #? Output: 0
#print(a.index("z")); #? Output: ValueError: substring not found

#* The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
#! Note: Space is not an alphanumeric character.
a = "aman123";
print(a.isalnum()); #? Output: True

#* The isalpha() method returns True if all the characters are alphabet letters (a-z).
a = "aman";
print(a.isalpha()); #? Output: True

#* The islower() method returns True if all the characters are in lower case, otherwise False.
a = "aman";
print(a.islower()); #? Output: True

#* The isupper() method returns True if all the characters are in upper case, otherwise False.
a = "AMAN";
print(a.isupper()); #? Output: True

#* The isprintable() method returns True if all the characters are printable, otherwise False.
a = "Hello! Are you #1?";
print(a.isprintable()); #? Output: True

#* The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
a = "   ";
print(a.isspace()); #? Output: True

#* The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
a = "Hello, And Welcome To My World!";
print(a.istitle()); #? Output: True

#* The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
a = "Hello My Name Is AMAN";
print(a.swapcase()); #? Output: hELLO mY nAME iS aman

#* The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
a = "Welcome to my world";
print(a.title()); #? Output: Welcome To My World

"""
    ! Note: All string methods returns new values. They do not change the original string.
    ! Note: Strings are immutable: Strings cannot be changed, only replaced.
"""