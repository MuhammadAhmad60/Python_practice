#Write a Python program that uses a lambda function to filter out all even numbers from
# a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("The list of even numbers are: ", filtered_numbers)