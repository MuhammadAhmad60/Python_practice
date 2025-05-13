#create a program that removes duplicates from a given list of
#integers without using the set data structure. Use for loop
#and if statement to check for duplicates.

numbers = [1,2,3,4,4,5,5,1,3,6,7,6]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"List after removing Duplicates: ", unique_numbers)
