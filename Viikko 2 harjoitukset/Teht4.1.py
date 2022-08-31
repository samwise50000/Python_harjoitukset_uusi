# Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

# Write a program that uses the while-loop,
# that prints numbers only dividable by 3 between numbers 1....1000

number = 1

while number <= 1000:
    number += 1
    if number % 3 == 0:
        print(number)
