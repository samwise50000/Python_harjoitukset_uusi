# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.


# Write a function, that gets a parameter of the pizza diameter and the value of pizza in euros.
# The function calculates and returns the value of pizza by euros per square meter.
# The main program asks the user two pizzas and the diameters of the pizzas and the prices. The program then informs,
# which one of the two pizzas you will get the better value for (basically which pizza has the cheaper value in total).
# The price unit calculation has to use a written function

import math


def calculatePizzaValuePerSquareMeter1(diameterInCm, priceInEuros):
    pizzaSurfaceArea = math.pi*diameterInCm
    priceInEuroPerSquareMetre = pizzaPriceInEuros1 / pizzaSurfaceArea
    return priceInEuroPerSquareMetre

def calculatePizzaValuePerSquareMeter2(diameterInCm, priceInEuros):
    pizzaSurfaceArea = math.pi*diameterInCm
    priceInEuroPerSquareMetre = pizzaPriceInEuros2 / pizzaSurfaceArea
    return priceInEuroPerSquareMetre

def calculateBestValueForMoneyPizza(pizza1PricePerSquareMetre, pizza2PricePerSquareMetre):
    if pizza1PricePerSquareMetre < pizza2PricePerSquareMetre:
        return print(f"Pizza 1 on halvempi, pizzan hinta on {pizza1PricePerSquareMetre:.2f}€ per neliömetri.")
    else:
        return print(f"Pizza 2 on halvempi, pizzan hinta on {pizza2PricePerSquareMetre:.2f}€ per neliömetri.")

pizzaDiameterInCm1 = float(input('Anna ensimmäisen pizzan halkaisija senttimetreinä: '))
pizzaPriceInEuros1 = float(input('Anna ensimmäisen pizzan hinta euroina: '))

pizzaDiameterInCm2 = float(input('Anna toisen pizzan halkaisija senttimetreinä: '))
pizzaPriceInEuros2 = float(input('Anna toisen pizzan hinta euroina: '))

pizza1PricePerSquareMetre = calculatePizzaValuePerSquareMeter1(pizzaDiameterInCm1, pizzaPriceInEuros1)
pizza2PricePerSquareMetre = calculatePizzaValuePerSquareMeter2(pizzaDiameterInCm2, pizzaPriceInEuros2)

bestValueForMoneyPizza = calculateBestValueForMoneyPizza(pizza1PricePerSquareMetre, pizza2PricePerSquareMetre)

