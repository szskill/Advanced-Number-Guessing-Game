from random import randint
import os

os.system("clear")

print(
    """
  _   _                 _                  _____                     _             
 | \ | |               | |                / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ 

"""
)

level = int(
    input(
        """
Enter the level you want to play
    [1.] Easy -> 10 attempts, number between 1 and 30.
    [2.] Medium -> 7 attempts, number between 1 and 40.
    [3.] Hard -> 5 attempts, number between 1 and 50.
    [4.] Custom mode -> Your choice of attempts, your choice of numbers.
Chloce: """
    )
)

i = 1

if level == 1:
    ip = 10
    c = 1
    b = 30
    print("You selected Easy mode.")
    print("You have 10 attempts.")

elif level == 2:
    ip = 7
    c = 1
    b = 40
    print("You selected Medium mode.")
    print("You have 7 attempts.")

elif level == 3:
    ip = 5
    c = 1
    b = 50
    print("You selected Hard mode.")
    print("You have 5 attempts.")

elif level == 4:
    print("Custom mode")
    c = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    ip = int(input("Enter the number of attempts: "))

else:
    print("Error 404")

a = randint(c, b)

while True:
    g = int(input(f"Guess a number between {c} and {b}: "))
    if g > a:
        print("Too high")
        i = i + 1
        ip = ip - 1
        print(f"You have {ip} attempts left.")
        if ip == 0:
            print("All attempts finished")
    elif a > g:
        print("Too low")
        i = i + 1
        ip = ip - 1
        print(f"You have {ip} attempts left.")
        if ip == 0:
            print("All attempts finished")
    elif a == g:
        print("Correct, You answered in", i, "attempts")
        print("Congrats, You have conpleted the game.")
        break
    elif g > b:
        print(f"Pls only choose a number between {c} and {b}")
        i = i + 1
        ip = ip - 1
        print(f"You have {ip} attempts left.")
        if ip == 0:
            print("All attempts finished")

    else:
        print("Error")
