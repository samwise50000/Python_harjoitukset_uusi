import random

def throwDice(throws):                                                                                                  #Function draws a number from 1 to given number
    diceNumber = random.randint(1,throws)
    return diceNumber

totalThrows = int(input("Kuinka monta tahkoa? "))                                                                       #Asks how many throws will be made

while True:
    numberDice = throwDice(totalThrows)
    print(numberDice)
    if numberDice == totalThrows:
        break