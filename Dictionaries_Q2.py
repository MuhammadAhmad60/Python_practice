#Create a program that takes a list of tuples (name, age)
# and creates a dictionary where names are the keys and ages are the values.

li = [("Bilal", 15), ("ALi", 24), ("Hassan", 20), ("Abu Bakar", 26)]

di = {}

for a, b in li:
    di[a] = di.get(a, []) + [b]

print(di)
