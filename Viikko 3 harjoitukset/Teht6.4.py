# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

# Write a function, that gets a parameter of a list of whole numbers.
# The program returns the sum of whole numbers in the llist.
# Write a main program for testing, where you create a list, and call the function to print out the sum inside the function.



def sumOfNumbers(listOfNumbers):
    sum = 0
    for number in listOfNumbers:
        sum += number
    return sum


listOfNumbers = [0, 5, 3, 2, 7, 11]

sum = sumOfNumbers(listOfNumbers)

print(f"Summa on: {sum}")


