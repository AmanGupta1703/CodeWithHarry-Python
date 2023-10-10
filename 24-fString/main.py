# What are f-strings?
# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
# Introduced from python 3.6

# Old Way
sentence = "My name is {1} and I'm from {0}."
country = "India"
name = "Aman"

print(sentence.format(country, name))

# New Way = f-strings
print(f"My name is {name} and I'm from {country}.")

print(f"{60 * 3}")

# How we use a f-string?
print(f"We use f-string like this: {{variable_name}}")

# Explanation
# Python will populate the values of the variables in the curly braces and print the string.

# f-strings are faster than the old way of formatting strings.
# f-strings are more readable than the old way of formatting strings.
