# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasemat = {}

def lentoasema():
    koodinlisäys=input("ICAO koodi: ")
    nimenlisäys=input("Lentoaseman nimi: ")
    lentoasemat[koodinlisäys] = nimenlisäys

def kerroasema():
    kysyntä = input("Anna ICAO koodi: ")
    if kysyntä in lentoasemat:
        print(f"Lentoasema on {lentoasemat[kysyntä]}.")
    else:
        print("Ei ole lentoasemaa.")


ensimmäinen = 1
print("1 - syötä uusi")
toinen = 2
print("2 - haku")
nolla = 0
print("0 - lopetus")
valinta = int(input("Valitse 1, 2 tai 0: "))
while valinta != nolla:
    if valinta == ensimmäinen:
        lentoasema()
    if valinta == toinen:
        kerroasema()
        if valinta == nolla:
            break
    valinta = int(input("Valitse 1, 2 tai 0: "))