
# What is a Set?
# A set is a collection which is unordered and indexed. In Python sets are written with curly brackets.
# Set is a collection of well-defined objects.

# Sets are unordered hence we cannot access elements using indexes.

# Creating a Set
s = {2, 4, 6, 2}

# Creating a empty set. If we use {} then it will create a empty dictionary.
# s = set()

sqaures = set()

for num in s:
    sqaures.add(num ** 2)
print(sqaures)

print(type(s))

