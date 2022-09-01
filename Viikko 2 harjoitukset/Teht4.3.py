# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

userInput = input('Anna luku. Ohjelma loppuu, kun annat tyhjän merkkijonon: ')
lowestNumber = 0
highestNumber = 0
index = 0

while userInput != "":

    number = int(userInput)
    if lowestNumber == 0:
        if index == 0:
            lowestNumber = number

    if highestNumber == 0:
        highestNumber = number

    if number < lowestNumber:
        lowestNumber = number

    if number > highestNumber:
        highestNumber = number

    index += 1

    userInput = input('Anna luku. Ohjelma loppuu, kun annat tyhjän merkkijonon: ')

print('Pienin syötetty luku: ' + str(lowestNumber))
print('Suurin syötetty luku: ' + str(highestNumber))
