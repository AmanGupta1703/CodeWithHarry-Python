
# Dictionary Methods

# Sets are unordered
# Dictionaries are ordered since Python 3.7

employee_1 = {
    700: 50,
    800: 60,
    900: 70,
    100: 80,
    200: 50
}

employee_2 = {
    200: 30,
    300: 40,
    400: 50,
}

# update() method => update the dictionary with the items from the given argument

# employee_1.update(employee_2)

# clear() method => remove all items from the dictionary

# employee_1.clear()

# pop() method => remove the item with the specified key name

employee_1.pop(700)

# popitem() method => remove the last inserted item

employee_1.popitem()

# del() method => remove the item with the specified key name. if the key does not exist, it will raise an error or if key is not provided, it will delete the dictionary completely

# del employee_1[700]

# del employee_1


print(employee_1)
