"""
Built-In string Methods :
         Python built-in functions are predefined functions that are permanently loaded into the Python interpreter at startup and are readily available for use anywhere in your code without requiring any import statements.

""" 

name = "Rahul"
# print(name.upper()) ----> capitalize the whole string
# print(name.lower())   ----> Converts a string into lower case
# print(name.capitalize())  -----> 	Converts the first character to upper case
# print(name.isalnum()) ----> Returns True if all characters in the string are alphanumeric
# print(name.islower()) ----> Returns True if all characters in the string are lower case
# print(name.isalpha()) ----> Returns True if all characters in the string are in the alphabet
# print(name.casefold()) ----> Converts string into lower case
# print(name.startswith(R)) ----> Returns true if the string starts with the specified value
# print(name.endswith("l")) ----> Returns true if the string ends with the specified value
# print(name.encode()) ----> Returns an encoded version of the string
# print(name.replace("Rahul", "Ramesh")) ----> Returns a string where a specified value is replaced with a specified value
# print(name.swapcase()) ----> Swaps cases, lower case becomes upper case and vice versa
# print(name.center(10)) ----> Returns a centered string
# print(len(name))
# print(len(name.center(20)))
#print(name.index("h")) ----> Searches the string for a specified value and returns the position of where it was found




name2 = "!!!Rahul!!!"
# print(name2.rstrip("!")) ----> Returns a right trim version of the string


a = "rahul ramesh patil"
# print(a.split(" ")) ----> Splits the string at the specified separator, and returns a list
# print(a.count("ra")) ----> Returns the number of times a specified value occurs in a string
# print(a.find("ra")) ----> Searches the string for a specified value and returns the position of where it was found
print()


s = " "
# print(s.isspace()) ----> Returns True if all characters in the string are whitespaces

p = " This Is The Python Language"
# print(p.istitle()) ----> Returns True if the string follows the rules of a title

