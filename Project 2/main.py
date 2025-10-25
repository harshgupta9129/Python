from random import randint

com = randint(1,101)
user = int(input("Guess The Number : "))
attempts = 1

while com!=user:
    if user > com :
        user = int(input(f"Please Enter Less Value than {user} : "))
    else :
        user = int(input(f"Please Enter Greater Value than {user} : "))
    attempts+=1

print(f"Hey You Guess it in {attempts} Attempts")