"""
SETS :
    In Python, a set is a built-in data structure used to store an unordered collection of unique, immutable elements.
    Can be written in {} Braces.
    Sets automatically eliminates the duplicate values.
    We can not access elements in sets using indexing and slicing.
    Empty curly brackets make a dictionary, not a set. 
    An empty set must be written set().
    Set items must be hashable, which for now simply means immutable

Syntax:
        fruits = {"Apple", "Banana"}
        print(fruits)
"""
# set()  ------> Empty set can be defined as Set()
# print(set)


# fruits = {}
# print(type(fruits)) -----> It can be consider as Dict


# a = {1, 2, 3}
# b = set([4, 4, 5])
# c = set("hello")
# d = set()
# print(a, b, d)
# print(sorted(c))


# Methods in Sets :
s1 = {11, 19, 27}

# s1.add(12) -----> adds one item (does nothing if already present)
# print(s1)

# s1.update([4, 9])
# print(s1)  ------> adds every item from another collection


# s1.remove(11) ----> removes 11, KeyError if missing
# print(s1)


# s1.discard(99) -----> removes x, no error if missing
# print(s1)


# s1.pop() -----> Removes the last element from the set
# print(s1)


# s1.clear() -----> Empties the set