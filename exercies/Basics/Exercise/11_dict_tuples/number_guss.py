import random

secret_number = random.randint(1, 100)

print("welcome to the number gussing game")
print("i am thinking of a number between 1 and 100")

attempts = 0

while True:
    guss = int(input("enter your guss : "))
    attempts += 1

    if guss < secret_number:
        print("too low")
    elif guss > secret_number:
        print("too high")
    else:
        print(f"you guss the number in {attempts} attempts")
        break
