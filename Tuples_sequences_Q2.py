#Write a Python function that takes two tuples as arguments and returns a
# new tuple that contains the elements common to both tuples.

tuple1 = (1,2,3,4,5,6)
tuple2 = (3, 4, 6, 7, 8)

def common_tuple(t1, t2):
    return tuple(x for x in t1 if x in t2)

result = common_tuple(tuple1, tuple2)

print("Common Elements are: ", result)