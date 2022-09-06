# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

for n in range(5):                                                                                                      #Käy läpi loopin 5 kertaa. n tarkoitus on olla väliaikane muuttuja
    kaupungit.append(input('Anna viisi kaupungin nimeä. '))

for x in kaupungit:
    print(x)