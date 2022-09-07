# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

# Write a function, that gets a parameter that gets USA gasoline in USA gallons and returns the value in liters.
# Write a main program, that asks the gallon amount from the user and then it turns them in liters. The change from gallons to liters has to be made by using the function (sub-procedure).
# The change will be made until the user inputs a negative gallon amount.



def convertToLiters(liters):
    result = gallons * 3.785
    return result

gallons = float(input('Ohjelma muuttaa antamasi lukeman Yhdysvaltain nestegalloneista litroiksi. Ohjelma lopettaa muuntelun, kun annat negatiivisen lukeman. Anna jokin lukema: '))

while gallons >= 0:
    liters = convertToLiters(gallons)
    print(f"{liters:.2f} litraa.")
    gallons = float(input('Ohjelma muuttaa antamasi lukeman Yhdysvaltain nestegalloneista litroiksi. Ohjelma lopettaa muuntelun, kun annat negatiivisen lukeman. Anna jokin lukema: '))

