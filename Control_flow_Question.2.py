#Q3: Create a program that prints the Fibonacci sequence up to a
#given number n using a for loop and range() function.
n = int(input("Enter the n number: "))

a , b = 0, 1

for _ in range(n):
    if a >= n:
        break
    print(a, end=' ')
    a,b = b, a+b