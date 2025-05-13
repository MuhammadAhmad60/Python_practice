#Write a Python program that uses the math module to calculate the square root of a number
# entered by the user.
import math

from fontTools.misc.cython import returns

num = int(input("Enter the number: "))

if num < 0:
    print("Enter the positive integer: ")
else:
    returns = math.sqrt(num)
    print(f" the square root " ,num, "is", returns)

