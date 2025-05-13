# Write a function sum_numbers(*args) that takes any number of numerical arguments and returns their sum.
# Test the function with a variable number of arguments.

def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1,2,3))
print(sum_numbers(22,45,66))
