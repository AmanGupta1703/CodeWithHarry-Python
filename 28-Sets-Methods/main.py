# What are Set Methods?
# Set methods are used to perform operations on sets.

# union() Method => Returns a set containing the union of sets

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

print(s1.union(s2))

# To Update s1 with the union of s1 and s2 we can use update() method
s1.update(s2)
print("Using the update() method", s1)

# intersection() Method => Returns a set, that is the intersection of two other sets (meaning the value which are common in both sets)
cities = {"Madrid", "Barcelona", "Valencia", "Seville"}
cities2 = {"Madrid", "Tokyo", "Barcelona", "Paris"}

common_cities = cities.intersection(cities2)

# intersection_update() Method => Removes the items in this set that are not present in other, specified set(s)
# includes items which are present in both sets and the items which are present in the first set
# cities.intersection_update(cities2)
# print(cities)

print(common_cities)

# symmetric_difference() Method => Returns a set with the symmetric differences (items which are not common in the two sets) of two sets

cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities2 = {"Madrid", "Tokyo", "Barcelona", "Paris"}

cities3 = cities.symmetric_difference(cities2)
print(cities3)

# symmetric_difference_update() Method => inserts the symmetric differences from this set and another
cities.symmetric_difference_update(cities2)

print(cities)

# difference() Method => Returns a set containing the difference between two or more sets
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities2 = {"Madrid", "Tokyo", "Barcelona", "Paris"}

cities3 = cities.difference(cities2)
print(cities3)

# isdisjoint() Method => Returns True if none of the items are present in both sets, otherwise it returns False
# disjoint => two sets are said to be disjoint sets if they have no common elements

cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities2 = {"Paris", "London", "New York"}

print(cities.isdisjoint(cities2))

# issuperset() Method => Returns True if all items in the set exists in the specified set, otherwise it returns False
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities2 = {"Madrid", "Tokyo", "Barcelona", "Paris"}

print(cities.issuperset(cities2))  # False

# issubset() => Returns True if all items in the set exists in the specified set, otherwise it returns False
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities2 = {"Madrid", "Tokyo"}

print(cities2.issubset(cities))  # True

# add() => Adds an element to the set
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities.add("Paris")
print(cities, "|| added a city named \"Paris\"")

# remove() => Removes the specified element
cities.remove("Paris")
print(cities, "|| removed a city named \"Paris\"")

# discard() => Removes the specified item
cities.discard("Tokyo")
print(cities, "|| removed a city named \"Tokyo\"")

# remove() VS discard()
# remove() will raise an error if the specified item does not exist
# discard() will NOT raise an error if the specified item does not exist

# pop() => Removes an element from the set
# This catch is that a random item is removed from the set, since sets are unordered
# we can get the removed item by storing it in a variable
removed_city = cities.pop()
print(removed_city)

# del() => Deletes the set completely
del cities

# clear() => Removes all the elements from the set
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
cities.clear()
print(cities)

# check if an item exists in a set
cities = {"Madrid", "Barcelona", "Valencia", "Tokyo"}
if "Tokyo" in cities:
    print("Tokyo is in the set.", "Moving to Tokyo...")
else:
    print("Tokyo is not in the set.")
