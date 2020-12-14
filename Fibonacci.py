a = 1
while a == 1:
    while True:
        n = input("Enter a number: ")
        if n.isdigit() == True:
            n = int(n)
            break
        print("You made a mistake. Try again.")

    fibonacci = 0
    number1 = 0
    number2 = 1
    while fibonacci <= n:
        print(fibonacci, end= "   ")
        fibonacci += number2
        number2, number1 = number1, fibonacci
    a = int(input("\nContinue - 1, Exit - else: "))

