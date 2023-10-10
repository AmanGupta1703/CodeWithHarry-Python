# What are tuples?
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Create a tuple:
tup = (1, 5, 6)
print(tup, type(tup))

# Creating a tuple with one element is a bit tricky.
new_tup = (1,)
print(tup, type(new_tup))

# Access tuple elements
print(tup[0])
print(tup[1])
print(tup[2])

print("Negative Indexing: ")

# Negative Indexing
print(tup[len(tup) - 1])
print(tup[-1])

# Check if an element exists in a tuple
if 5 in tup:
    print("It's present in the tuple! YAY!!")

# Slicing a tuple
print(tup[0:])  # Prints all elements
print(tup[:1])  # Prints first element

print(tup[0:2])  # Prints first two elements

# Changing a tuple
# Tuples are unchangeable, or immutable as it also is called.
# We can't change the length of the tuple, but we can change its content.

# tup[0] = 2 # This will give an error
