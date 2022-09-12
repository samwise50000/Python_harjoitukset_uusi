# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa, joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi. ")
        nimi = input("Anna uusi nimi: ")
        if nimi == "":
            break
    else:
        nimet.add(nimi)
        if nimi == "":
            break
    nimi = input("Anna uusi nimi: ")
for x in nimet:
    print(x)