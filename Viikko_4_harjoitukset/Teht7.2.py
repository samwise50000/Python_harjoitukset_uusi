# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa, joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.



nimet = set()
nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
    nimi = input("Anna uusi nimi: ")

for i in nimet:
    print(i)