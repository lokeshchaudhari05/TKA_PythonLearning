"""
TUPLE :
    Tuple is an In-built collective data type in python which stores multiple values/Data in a single variable.
    Tuple can be defined using () brackets.
    Tuple is immutable but if we want to change something then we convert the tuple into list.
    Tuple follows an insertion order.
    Tuple can hold values with the different data types.
    Items are seperated by the commas.
    Allows duplicate values.

    Syntax :
    list_name = ('value-1','value-2','value-3')
    list_name = () ----> Empty list

"""
# Tuple only have 2 Built-In methods :
t1 = (14, 19, 35, 57, 72, 35, 89, 98, 35)
# print(t1.count(35)) ----> Returns the count of the specified value
# print(t1.index(35)) ----> Returns the index number of specified value


# t2 =() ----> Empty Tuple
# t3 = ("rakesh") ----> considered as string not tuple
# t4 = 12,  ----> Tuple without circular braces and comma seperate values


# t = (1, [2, 3])
# t[1].append(4) ----> . If an item inside is a mutable object like a list, that list can still change.
# print(t)


# t = (10, 20, 30, 20)
# print(t.count(20))
# print(t.index(20))
# print(20 in t)
# print(len(t), min(t), max(t), sum(t))


# Concept of Packing & Unpacking
# point = (3, 4)
# x, y = point
# print(x, y)

# t1 = (11,12,13,14,15,20)
# first, *middle, last = t1
# print(first)
# print(middle)
# print(last)


# students = [("Aisha", 85), ("Rahul", 72), ("Priya", 91)]

# best_name, best_mark = students[0]
# total = 0

# for name, mark in students:
#     total += mark
#     if mark > best_mark:
#         best_name, best_mark = name, mark

# print(f"Top scorer: {best_name} ({best_mark})")
# print(f"Average: {total / len(students):.1f}")