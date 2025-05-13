#Write a function factorial(n) that takes an integer n and returns the factorial
# of the number. The function should handle the case where n is negative by
# raising an appropriate exception.


def fact(n):
    if n < 0:
        raise ValueError("Enter the positive Number: ")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(fact(5))