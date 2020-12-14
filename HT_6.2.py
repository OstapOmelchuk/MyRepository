from math import pi, sqrt

def rectangle_square(a, b):
    return a * b

def triangle_square(a, b, c):
    p = (a + b + c)/2
    return sqrt(p * (p - a) * (p - b) * (p - c))

def circle_square(R):
    return pi * R**2

n = "1"
while n == str(1):
    choice = input("""
What do you want to calculate:
1 - the square of a rectange
2- the square of a triangle
else - the square of the circle
""")
    if choice == str(1):
        a, b = -1, -1
        while a <= 0 or b <= 0:
            print("The length of the sides must me > 0!")
            a = int(input("Enter a: "))
            b = int(input("Enter b:"))
        print(rectangle_square(a, b))
    elif choice == str(2):
        a, b, c = -1, -1, -1
        while a + b <= c or b + c <= a or a + c <= b or a <= 0 or b <= 0 or c <= 0:
            print("the sum of the length of two sides must be bigger than the length of the 3rd and the length of each side must bigger than 0!")
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            c = int(input("Enter c: "))

        print(triangle_square(a, b, c))
    else:
        R = -1
        while R <= 0:
            print("The length of the radius must be > 0")
            R = int(input("Enter R: "))
        print(circle_square(R))
    n = input("1 - continue, else - exit: ")
    