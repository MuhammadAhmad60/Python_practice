#Write a Python program that accepts a tuple of numbers from the user
#and returns the sum of all the numbers in the tuple.

user_input = input("Enter the numbers seprate by commas: ")

numbers = tuple(int(x.strip()) for x in user_input.split(','))

total = sum(numbers)

print("the total sum of numbers is: ", total)
