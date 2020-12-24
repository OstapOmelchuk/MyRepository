import Module_1 as m1

n = "1"
while n == str(1):
    choice = input("""
What do you want to calculate:
1 - the square of a rectange
2 - the square of a triangle
else - the square of the circle
Enter your choice: """)
    if choice == str(1):
        a, b = -1, -1
        while a <= 0 or b <= 0:
            print("The length of the sides must me > 0!")
            a = int(input("Enter a: "))
            b = int(input("Enter b:"))
        print(m1.rectangle_square(a, b))
    elif choice == str(2):
        a, h = -1, -1
        while a <= 0 or h <= 0:
            print("the hight and the 'a' side must be bigger than 0!")
            a = int(input("Enter a: "))
            h = int(input("Enter h: "))
        print(m1.triangle_square(a, h))
    else:
        R = -1
        while R <= 0:
            print("The length of the radius must be > 0")
            R = int(input("Enter R: "))
        print(m1.circle_square(R))
    n = input("1 - continue, else - exit: ")
    