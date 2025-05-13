# Write a Python program that uses a lambda function to sort a list of
# tuples based on the second value in each tuple.

data = [(1, 5), (3, 2), (4, 8), (2, 1)]


sorted_data = sorted(data, key=lambda x:x[1])

print("Sorted the data according to second value: " , sorted_data)