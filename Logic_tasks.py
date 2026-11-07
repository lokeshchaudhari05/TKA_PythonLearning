# write the python programm to remove duplicate elements from a list without using set()
# my_list = [10, 20, 30, 10, 40, 20, 50]
# new_list = []

# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)

# print("Original List: ",my_list)
# print("New list",new_list)



# write a programm to find the second largest element from list without using sort(), sorted() or max()
# numbers = [10, 25, 50, 40, 30, 60]

# largest = numbers[0]
# second_largest = None

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i

#     elif i < largest:
#         if second_largest == None or i > second_largest:
#             second_largest = i

# print("Largest element:", largest)
# print("Second largest element:", second_largest)



# write the progaramm to seperate even and odd numbers from the list
# numbers = [10, 25, 50, 40, 30, 60]

# even = [n for n in numbers if n % 2 == 0]
# odd = [n for n in numbers if n % 2 != 0]

# print("even: ",even)
# print("odd: ",odd)



# programm to count how many times each element occur in list
# from collections import Counter

# items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counts = Counter(items)

# print(counts)



# write the programm to reverse the tuple
# original_tuple = ("apple", "banana", "cherry")
# reversed_tuple =tuple(reversed(original_tuple))
# print(reversed_tuple)


# programm to find maximum and minimum 
# numbers = (45, 12, 89, 3, 67, 21)

# max_val = numbers[0]
# min_val = numbers[0]

# for num in numbers[1:]:
#     if num > max_val:
#         max_val = num
#     elif num < min_val:
#         min_val = num

# print("Maximum value:", max_val)
# print("Minimum value:", min_val)