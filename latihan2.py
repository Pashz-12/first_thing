# 23 - 11 - 2025
# generate number
# guess number
# if number > tebakan
#  too high
# elif number < tebakan
#  too low
# elif number == tebakan
#  you right
# break
# invalid option does not decrease attempts
# Latihan di masa masa gabut, masih berantakan bgt ini

import random

beginning = True
tebakan = random.randint(1,100)
while beginning:
    try:
        pre_attempts = input("Would you like to set your attempts or random it? (y/n): ").lower()
        if pre_attempts == "y":
            attempts = int(input("How many attempts do you wanna guess: "))
            beginning = False

        elif pre_attempts == "n":
            attempts = random.randint(1,20)
            beginning = False

        else:
            print("Invalid option")

    except ValueError:
        print("Invalid option")
            



while attempts >0:
    try:
        jawaban = int(input("Guess the number beetween 1 - 100 : "))
            
        if jawaban > tebakan:
            print("Too high")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")


        elif jawaban < tebakan:
            print("Too low")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

            
        elif jawaban == tebakan:
            print("Congratulations, you guess the number")
            print(f"Total attempts: {attempts}")
            break


    except ValueError:
        print("Invalid option")
        print(f"Total attempts remaining: {attempts}")

