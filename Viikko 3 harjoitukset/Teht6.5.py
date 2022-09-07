# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

# Write a function, that gets a list of whole numbers into the parameter.
# The program will return another list, that is same as in the parameter BUT it has every odd number removed.
# Write a main program, where you create a list. Call out the function and then print out in the main program the first original list and then the list that has odd numbers removed.

def removeOddNumbers(listOfNumbers):
    list = []

    for number in listOfNumbers:
        if (number%2 == 0):
            list.append(number)
    return list

listOfNumbers = [0, 3, 4, 6, 7, 13, 16, 19, 21, 23]

listOfEvenNumbers = removeOddNumbers(listOfNumbers)

print(listOfNumbers)
print(removeOddNumbers(listOfNumbers))