# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

# Write a game, where computer draws an integer between 1..10.
# The computer tries to guess the integer as long as it guesses it right.
# After each guess, the program will print out text "Too high guess", "Too low guess", or "Correct."
# Attention! The computer can't switch the integer between the draws.
import random

userInput = int(input('Ohjelma on arvonnut luvun välillä 1-10. Yritä arvata oikea luku: '))
rNumber = random.randint(1, 10)

while userInput != rNumber:
    userInput = int(input('Uusi yritys: '))
    if rNumber < userInput:
        print("Liian suuri arvaus")
        if rNumber == userInput:
            ("Oikein.")

    elif rNumber > userInput:
            print("Liian pieni arvaus")
    else:
                print("Oikein.")






