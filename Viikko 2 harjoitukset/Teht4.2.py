# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan ,
# kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.

inches = int(input('Anna tuuma numero kokonaislukuna. Ohjelma loppuu, kun annat negatiivisen tuuman kokonaislukuna: '))

while inches >= 0:
    print(inches * 2.54)
    inches = int(input('Anna tuuma numero kokonaislukuna. Ohjelma loppuu, kun annat negatiivisen tuuman kokonaislukuna: '))