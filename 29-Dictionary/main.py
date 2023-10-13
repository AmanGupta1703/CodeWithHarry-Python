# What is a Dictionary?
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Since Python 3.8, dictionaries are ordered. In Python 3.7 and earlier, dictionaries are unordered.

english_dictionary = {
    "name": "English",
    "countries": ["United States", "United Kingdom", "Australia", "Canada", "New Zealand", "Ireland", "South Africa"],
    "speakers": 1121,
    "alphabet": "Latin",
    "family": "Indo-European",
}

# Print a Dictionary
print(english_dictionary)

# Accessing a Single Item from a Dictionary
print(english_dictionary["name"])
print(english_dictionary["alphabet"])

# If you try to access a key that does not exist, you will get an error.
# print(english_dictionary["population"])

# Accessing Items Using get()
print(english_dictionary.get("name"))

# If the key does not exist, you will get the value None. (when we use get() to get the value of a key that does not exist)

# Getting all the Keys in a Dictionary
print(english_dictionary.keys())  # dict_keys(['name', 'countries', 'speakers', 'alphabet', 'family'])

# Getting all the Values in a Dictionary
print(english_dictionary.values())

# Looping through all the Keys in a Dictionary
print()
for key in english_dictionary.keys():
    print(f"{key}: {english_dictionary.get(key)}")

# Getting all the Items in a Dictionary
print(english_dictionary.items())

print("\nLooping through all the items in a dictionary. using the \"items()\" method\n")
# Looping through all the Items in a Dictionary
for key, value in english_dictionary.items():
    print(f"{key}: {value}")
