import random
import string

anu_input = input("Enter the length of the password you want: ")

if anu_input.isdigit():
    length = int(anu_input)
    
    if length > 0:
        anu_set = string.ascii_letters + string.digits
        password = ''.join(random.choices(anu_set, k=length))
        print("Generated password is:", password)
    else:
        print("Length must be greater than zero and cannot be negative.")
else:
    print("Length can only be a positive whole number not string.")
