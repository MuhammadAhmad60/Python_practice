#Write a Python program to reverse a list of numbers using a list comprehension.

num = [1, 2, 3, 4, 5, 7]

reversed_list = [x for x in num[:: -1]]

print(f"The reversed list is ", reversed_list)