# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
#for number in numbers[:5]:
    #print(number)


numbers = []
readingNumbers = True
while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))

numbers.sort(reverse=True)
print(numbers[0:5])
