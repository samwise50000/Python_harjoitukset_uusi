# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Write a program, that asks the user numbers up to the point,
# until the user inputs an empty string as the ending mark.
# After the program ends, the program will output the lowest and highest number that was given.

userInput = input('Enter a number, or enter a blank string to stop: ')
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

    userInput = input('Enter a number, or enter a blank string to stop: ')

print('Lowest number: ' + str(lowestNumber))
print('Highest number: ' + str(highestNumber))
