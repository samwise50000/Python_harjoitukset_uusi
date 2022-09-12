nimet = set()
nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
        nimi = input("Anna nimi: ")
        if nimi == "":
            break
    else:
        nimet.add(nimi)
        if nimi == "":
            break

for x in nimet:
    print(x)