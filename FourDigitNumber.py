while True:
    num = input("Enter 4-digit number: ")
    if len(num) == 4 and num.isdigit() == True:
        num = int(num)
        break
    print("You made a mistake. Try again.")

ones = num % 10
tens = num  % 100 // 10
hundreds = num // 100 % 10
thousands = num // 1000
#print(thousands, hundreds, tens, ones)

mult = ones * tens * hundreds * thousands
print(f"{thousands} * {hundreds} * {tens} * {ones} = {mult}")
num1 = 1000 * ones + 100 * tens + 10 * hundreds + thousands
print(f"Reversed: {num1}")
lst = [ones, tens, hundreds, thousands]
lst.sort()
print("Sorted: ", end = "")
for el in lst:
    print(el, end= " ")