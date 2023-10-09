
# List Methods (List Functions)

l = [56, 12, 15, 65, 23];

#? append() method => add an element to the end of the list
# l.append(98);

#? sort() method => sort the list
# l.sort();
# l.sort(reverse=True); #? sort the list in reverse order

#? reverse() method => reverse the list
# l.reverse();

#? index() method => return the index of the element
print(l.index(12));

#? copy() method => return a copy of the list
new_list = l.copy();
new_list[0] = 100;

#? insert() method => insert an element at the specified index
l.insert(1, 899);

#? extend() method => add the elements of a list to the end of the current list

colors= ['red', 'green', 'blue'];
rainbow = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"];

colors.extend(rainbow);
print(colors);

#? Cocatenation of two stirngs
first_names = ["John", "Jane", "Jack"];
last_names = ["Doe", "Doe", "Doe"];

print(first_names + last_names); #?

print(l);