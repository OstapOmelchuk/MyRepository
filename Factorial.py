import matplotlib.pyplot as plt
import numpy
a = 1
while a == 1:
    while True:
        num = input("Enter a number: ")
        if num.isdigit() == True:
            num = int(num)
            break
        print("You made a mistake. Try again.")

    fuctorial = 1
    for i in range(num):
        fuctorial *= i+1
        
    print(f"fuctorial of {num} = {fuctorial}") 
    a = int(input("""Continue - 1, Exit - else: """))