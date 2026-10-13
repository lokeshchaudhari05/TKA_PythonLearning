"""
String : a string is an immutable sequence of Unicode characters used to handle and represent textual data.
         can be defined using single Quote, Double Quote and triple quotes.
         string in python is immutable.
         White space is also consideres as character in string.
      
text = 'python is dynamic language'
text2 = "python is an dynamic language"
text3 = '''python is an dynamic language'''
"""

"""
Indexing : Indexing in Python is an operation that allows you to access or retrieve individual items within an ordered  sequence—such as a list, tuple, string, or array—by referring to their specific position. 
     Python supports two main forms of positional indexing:
         1. Zero-Based (Positive) Indexing:
             meaning the first item of a sequence starts at position 0, the second item is at position 1, and so on.
         2.Negative Indexing:
             indexing start with the (-1) from last character in string


text = "python is a dynamic language"
print(len(text))
print(text[0])
print(text[7])
print(text[-1])
print(text[-10])
"""


"""
Slicing : Slicing cuts out a part of a string and gives you a new string.
          Slicing refers to the retriving of the specific part from the string.
          The fundamental rule of slicing is the syntax:
            sequence[start:stop:step] 
          -start (Inclusive): The index where the slice begins. Defaults to 0 (the first element) if omitted
          -(Exclusive): The index where the slice ends. The element at this index is not included in the output.     Defaults to the end of the sequence if omitted.
          -step (Stride): The step size or increment interval. Defaults to 1 if omitted

word = "PYTHON"
print(word[1:4])
print(word[0:2])
print(word[2:6])
print(word[:3])
print(word[3:])
print(word[:])
print(word[-3:])
print(word[:-1])
print(word[-4:-1])
print(word[0:5:2])
"""



#practice qestions based on string and indexing:
#Write a Python program to print the length of the string "Python"
# lang = "python"
# print(len(lang))


#Write a program to print the first and last characters of "Programming" using positive indexing
# random = "programming"
# print(random[0])
# print(random[10])


#Find the output:
# s = "Computer"
# print(s[2])
# print(s[5])
# print(len(s))


#Write a program to print the first three characters of "Education" using positive indexing
# text = "education"
# print(text[0] + text[1] + text[2])


#Find the output:
# s2 = "Hello World"
# print(s2[-1])
# print(s2[-3])
# print(len(s2))


#Write a program to print the middle character of "Python" using len() and indexing
# text2 = "developer"
# secon_from_start = text2[1]
# second_from_end = text2[-2]
# print(secon_from_start)
# print(second_from_end)


#Find the output:
# s3 = "Python Programming"
# print(s3[7])
# print(s3[-7])
# print(len(s3))


#Write a program to accept a string from the user and print its length, first character, and last character
# text3 = "python"
# midle_index = len(text3) // 2
# print(text3[midle_index])


#Find the output:
# s = "Kiran Academy"
# print(s[5])
# print(s[-5])
# print(s[0])
# print(s[-1])


#Write a program to accept a string from the user and print its length, first character, and last character
# text4 = input("Enter the input string: ")
# print(len(text4))
# print(text4[0])
# print(text4[5])


#Find the output:
# s = "Artificial Intelligence"
# print(len(s))
# print(s[10])
# print(s[-10])


#Write a program to print the third character from the beginning and the third character from the end of "Information"
# text5 = "information"
# third_from_start = text5[2]
# third_from_end = text5[-3]
# print(third_from_start)
# print(third_from_end)


#Find the output:
# s = "123456789"
# print(s[4])
# print(s[-4])
# print(s[len(s) - 1])
# print(s[-len(s)])


#Write a program to accept a string from the user and print its length, first character, last character, second         character, and second-last character
# text6 = input("Enter the input string: ")
# print(len(text6))
# print(text6[0])
# print(text6[-1])
# print(text6[1])
# print(text6[-2])


#Find the output:
# s = "Programming"
# print(len(s))
# print(s[10])
# print(s[-11])
# print(s[11])




#practice questions based on indexing:
