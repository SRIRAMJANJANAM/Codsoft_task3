import random
import string

def generate_pwd():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    digits = string.digits
    sc = string.punctuation
    pwd = lc + uc + digits + sc
    password = ''.join(random.choices(pwd, k=length))
    print(f"Your generated password is: {password}")

generate_pwd()
