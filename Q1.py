#1. Using Python as a Calculator
#Q1: Write a Python program that takes two numbers as input from the user and performs
# the following operations: addition, subtraction, multiplication, division,
# and modulus. Display the results in a formatted manner.
num1 = float(input("Enter the Number1: "))
num2 = float(input("Enter the Number2: "))

operator = (input("Enter the Operator  (+, -, *, /,): "))


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
else:
    print("Enter the valid value")




