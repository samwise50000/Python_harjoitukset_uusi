# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

# Write a function, that gets a parameter that gets USA gasoline in USA gallons and returns the value in liters.
# Write a main program, that asks the gallon amount from the user and then it turns them in liters. The change from gallons to liters has to be made by using the function (sub-procedure).
# The change will be made until the user inputs a negative gallon amount.



def convertToGallons(liters):
    gallons = liters * 0.264172
    print(gallons)

liters = float(input('Anna bensiinin määrä. Ohjelma muuuttaa Yhdysvaltain nestegallonit litroiksi ja tulostaa sen. Ohjelma loppuu, kun annat negatiivisen lukeman: '))

while liters >= 0:
    convertToGallons(liters)

    liters = float(input('Anna bensiinin määrä. Ohjelma muuuttaa Yhdysvaltain nestegallonit litroiksi ja tulostaa sen. Ohjelma loppuu, kun annat negatiivisen lukeman: '))

