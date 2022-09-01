# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

# Write a game, where computer draws an integer between 1..10.
# The computer tries to guess the integer as long as it guesses it right.
# After each guess, the program will print out text "Too high guess", "Too low guess", or "Correct."
# Attention! The computer can't switch the integer between the draws.
import random

randomNumber = random.randint(1, 10)
userInput = int(input('Ohjelma on arvonnut luvun välillä 1-10. Yritä arvata oikea luku: '))

while userInput != randomNumber:
    if userInput < randomNumber:
        print("Liian pieni arvaus")

    else:
        print("Liian suuri arvaus")

    userInput = int(input('Ohjelma on arvonnut luvun välillä 1-10. Yritä arvata oikea luku: '))

print('Oikein.')
