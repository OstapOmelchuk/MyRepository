week = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

flag = True
while flag:
    try:
        day = int(input("Enter number from 1 to 7: "))
        if TypeError:
            raise TypeError("Expected int() value.")
        elif day <= 0:
            raise ValueError("Enter the positive number!")
        elif day >= 8:
            raise ValueError("Enter the number less than 8!")
        else:
            print(week[day])

    except ValueError as e:
        print(f"ValueError! {e}")  

    except TypeError as e:
        print(f"TypeError. {e}")
    flag = int(input("Exit? 0 - Yes, else - No: "))