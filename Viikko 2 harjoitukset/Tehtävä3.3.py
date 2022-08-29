#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja
#hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
#onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Sukupuolesi (nainen/mies)? ")
hg_value = int(input("Hemoglobiinisi (g/l)? "))

if gender == "nainen":
    # testataan naisen ohjearvot
    if hg_value < 117:
        print("Hemoglobiinin arvo on alhainen.")
    elif hg_value <= 175:
        print("Hemoglobiinin arvo on normaali.")
    else:
        print("Hemoglobiinin arvo on liian korkea.")
elif gender =="mies":
    # miehen arvot
    if hg_value < 134:
        print("Hemoglobiinin arvo on alhainen.")
    elif hg_value <= 195:
        print("Hemoglobiinin arvo on normaali")
    else:
        print("Hemoglobiinin arvo on liian korkea.")
