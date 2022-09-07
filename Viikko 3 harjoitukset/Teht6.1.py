import random

#def noppa():
#    noppaluku = 0
#    while noppaluku != 6:
#        noppaluku = random.randint(1, 6)
#        print(noppaluku)

#noppa()

def throwDice():
    diceNumber = random.randint(1, 6)
    return diceNumber

while True:
    numberDice = throwDice()
    print(numberDice)
    if numberDice == 6:
        break


