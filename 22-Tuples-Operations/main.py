# For performing any operations on a tuple,
# First we need to convert it into a list
# Then we can perform any operation on it
# Then we can convert it back to a tuple

# Example 1
countries = ("India", "China", "Russia", "Japan", "Poland")
list_countries = list(countries)
list_countries.append("Germany")  # Add Germany
list_countries.pop(4)  # Remove Poland
countries = tuple(list_countries)  # Convert back to tuple
print(countries)

asian_countries = ("India", "China", "Japan")
europium_countries = ("Poland", "Germany", "Russia")

all_countries = asian_countries + europium_countries
print(all_countries)

# Few Methods on a tuple

# count() - Returns the number of times a specified value occurs in a tuple.
print(all_countries.count("India"))  # Returns 1.

# index() - Searches the tuple for a specified value and returns the first position of where it was found.
# If not found, it will throw an error.
print(all_countries.index("Germany"))  # Returns 4.

# len() - Returns the length of the tuple.
print(len(all_countries))


# Important Note:
# Tuples are immutable, so we cannot add or remove elements from it.
# But we can add, remove or change elements in a list.
# So, we can convert a tuple into a list, perform any operation on it and then convert it back to a tuple.
# This is the only way to perform any operation on a tuple.

