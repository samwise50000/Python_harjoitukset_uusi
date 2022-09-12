# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='SeOnSiina!?',
         autocommit=True
         )

icao = input("Anna lentokentän ICAO-koodi")
sql = "SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"

cursor = yhteys.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for rivi in result:
    print(f"{result[0]}, {rivi[1]}")