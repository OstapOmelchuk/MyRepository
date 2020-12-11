name = input("What is Your name? : ")
age = input("How old are you? : " )
while age.isdigit() == False:
    age = input("Try again! How old are you? : " )
age = int(age)
place = input("Where do you live? : ")

print(f"""
Hello, {name}!
Your age is {age}.
You live in {place}.
""")