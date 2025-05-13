#Write a function that takes a list of strings and returns the longest string from the list.
# Handle the case where the list is empty.

def longest_string(strings):
    if not strings:
        return None
    return max(strings, key=len)
print(longest_string(['apple', 'mango', 'orange', 'dragonfruit', 'pineapple' ]))
