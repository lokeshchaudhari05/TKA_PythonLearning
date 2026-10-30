"""
DICTIONARIES :
    Dictionary is an built-in Data Type in python used to store multiple Element/Data within a single variable.
    Uses {} for defining the Dictionary.
    A dictionary is a collection of data stored in key-value pairs.
    Maintains insertion order.
    we can store values with the different data types.
    KEY must be UNIQUE and VALUE can allow DUPLICATES.
    It does not support the indexing and slicing but if we need a position access.
    Dictionary is mutable.

    Syntax:

        dictionary_name = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
}

"""
# D = {}
# print(D) ---->Returns the Empty Dictionary 

# employee = { "name": "Alice",  "age": 30,  "role": "Engineer"}
# print(employee)

# employee["city"] = "mumbai" ----> Adding the Dictionary
# print(employee)

# employee ["age"] = 19 ----> Updating the new Key-Value pair in dictionary
# print (employee)

# All 11 methods in Dictionary :
emp_info = {"name" : "Rahul", "Age" : 24, "city" : "mumbai", "salary" : 55000}

# print(emp_info.get("name")) ----> returns the value associated to key and missing key returns None or default

# print(emp_info.keys()) ----> shows the all keys

# print(emp_info.values()) ----> Provides all values in dictionary

# print(emp_info.items()) ----> Provides all key value pairs

# print(emp_info.update()) ----> Add or update pairs

# print(emp_info.pop("Age")) ---->Removes the key an returns the value
# print(emp_info)

# print(emp_info.popitem()) ---->Removes and returns the last element inserted
# print(emp_info)

