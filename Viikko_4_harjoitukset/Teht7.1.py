# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


kuukaudet = ("Tammikuussa on vuodenaikana talvi", "Helmikuussa on vuodenaikana talvi", "Maaliskuussa on vuodenaikana kevät",
             "Huhtikuussa on vuodenaikana kevät", "Toukokuussa on vuodenaikana kevät", "Kesäkuussa on vuodenaikana kesä",
             "Heinäkuussa on vuodenaikana kesä", "Elokuussa on vuodenaikana kesä", "Syyskuussa on vuodenaikana syksy", "Lokakuussa on vuodenaikana syksy",
             "Marraskuussa on vuodenaikana syksy", "Joulukuussa on vuodenaikana talvi")

kuukaudennumero = int(input("Anna kuukauden numero väliltä 1-12. Ohjelma kertoo, mikä vuodenaika on meneillään kyseisellä kuukaudella: "))
kuukausi = kuukaudet[kuukaudennumero - 1]
print (f"{kuukausi}")
