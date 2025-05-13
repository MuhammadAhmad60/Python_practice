#Write a Python program using a function to calculate the area of a rectangle.
#The function should accept length and width as arguments and return the area.

def calculate_area(length, width):
    return length *  width

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))


area = calculate_area(length, width)
print(f"The Area of a rectangle: " , area)
