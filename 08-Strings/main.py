
#? What is String?
#* String is a sequence of characters.
#* String is a data type in python.
#! String is immutable.

#? How to create a string?
#* String can be created by using single quotes or double quotes.
#* Example:
#* 'Hello World'
#* "Hello World"

#? How to create a multiline string?
#* String can be created by using triple quotes.
#* Example:
#* '''Hello World'''

# Creating a string
string = 'Hello World'
print(string)

# Creating a multiline string
multiline_string = '''Hello World
This is a multiline string'''
print(multiline_string)

# Having Double and Single Quotes in a string
string_quotes = 'Hello "World"'
print(string_quotes)

# Accessing a character in a string
string = 'Hello World'
print(string[0]) # Output: H

# Looping through a string
string = 'Hello World'
for character in string:
    print(character)
#! String is like a list of characters.

"""
# Output:   
    - Hello World
    - (Hello World
      This is a multiline string)
    - Hello "World"
    - H
    - H
      e
      l
      l
      o
       
      W
      o
      r
      l
      d
"""

#? Important Points
#* String is immutable.
#* String can be created by using single quotes or double quotes.
#* String can be created by using triple quotes.
#* String can contain single quotes or double quotes.
#* String can be accessed by using index.
#* String can be looped through.