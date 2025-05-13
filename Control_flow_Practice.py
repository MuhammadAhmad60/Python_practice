#Q2: Write a Python program that takes an integer input from the user and prints
# whether it is prime or not using if and for loops.

num = int(input("Enter the number: "))

is_prime = num > 1
i = 2

while i < num and is_prime:
    is_prime = (num % i != 0 ) and is_prime
    i += 1

print(f"{num} is a prime number.") if is_prime else print(f"{num} is not a prime number.")

