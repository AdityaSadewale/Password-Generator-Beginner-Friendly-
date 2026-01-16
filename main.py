# this is an simple password genreter usin sum key 

import random
password ="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890adcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}[]-:"

lenght_password = int(input("Enter the lenght of the password"))

a = "". join(random.sample(password,lenght_password))

print(f"Your password is {a}")

#the command to run thid code is an  python filename.py
