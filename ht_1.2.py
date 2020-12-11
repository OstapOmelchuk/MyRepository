a = input("Enter a: ")
while a.isdigit() == False:
        a = input("Enter a (digit): ")
a = int(a)
b = input("Enter b: ")
while b.isdigit() == False:
        b = input("Enter b (digit): ")
b = int(b)
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** b = {a ** b}")