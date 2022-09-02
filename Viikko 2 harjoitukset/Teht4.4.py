# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

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
