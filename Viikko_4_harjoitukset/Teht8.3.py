# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

from geopy.distance import geodesic
import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='SeOnSiina!?',
         autocommit=True
         )

def hae(lentoasema):
    sql = "select latitude_deg, longitude_deg from airport where ident = '" + lentoasema + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

x=input("Anna ensimmäinen ICAO-koodi: ")
x=x.upper()
hae(x)
y=input("Anna toinen ICAO-koodi: ")
y=y.upper()
hae(y)
print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa.")