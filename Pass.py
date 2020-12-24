import string as st
import re

flag = True
while flag:
    k = 0
    password = input("Enter your password: ")  
    if len(password)<6 or len(password)>16:
        k += 1
    elif not re.search("[a-z]",password):
        k += 1
    elif not re.search("[0-9]",password):
        k += 1
    elif not re.search("[A-Z]",password):
        k += 1
    elif not re.search("[$#@]",password):
        k += 1
    elif re.search("\s",password):  
        k += 1

    if k == 0:
        print(f"{password} is valid password")
        break
    else:
        print(f"{password} is invalid password")
        flag=True    