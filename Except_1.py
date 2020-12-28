def input_check(age):
    if age < 1:
        raise ValueError("Your age must be a POSITIVE NUMBER bigger than 0.")
    elif age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
    

Exit = 1
while Exit:
    try:
        age = int(input("Enter your age: "))    
        input_check(age)
    except ValueError as e:
        print("ValueError.", e)
    # except TypeError as e:
    #     print("TypeError. Your age must be a number!")
    Exit = int(input("Exit? 0 - Yes, else - No: "))
