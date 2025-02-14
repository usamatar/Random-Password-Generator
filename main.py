import random 
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"

length_password = int(input("Enter the length of your password "))
a = "".join(random.sample(password, length_password))
print("Your random password is " + a)