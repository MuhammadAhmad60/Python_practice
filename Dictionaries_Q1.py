#Write a Python program that takes a string as input and counts the frequency of each
#character in the string using a dictionary. Display the frequency count for each character.

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char]  = 1
print("\n frequency")
for char, count in frequency.items():
    print(f"'{char}': {count}")