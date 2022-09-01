# Toteutetaan algoritmi piin (π) likiarvon laskemiseksi.
# Oletetaan, että A on yksikköympyrä eli ympyrä, jonka keskipiste on origossa ja jonka säde on yksi.
# Sen ympärille piirretään pienin mahdollinen neliö B siten, että ympyrä A jää kokonaan neliön sisäpuolelle.
# Neliön nurkkapisteet ovat tällöin (-1,-1), (1,-1), (1,1) ja (-1,1).
# Jos neliön sisälle arvotaan satunnaisesti suuri määrä pisteitä,
# osuu niistä myös ympyrän sisälle likimain niin suuri osuus kuin ympyrän pinta-ala on neliön pinta-alasta eli πr^2/4,
# joka (koska ympyrän säde on yksi) sievenee muotoon π/4.
# Tästä saadaan yksinkertainen menetelmä piin likiarvon laskemiseksi:
# Arvotaan neliön B sisälle suuri määrä satunnaisissa kohdissa olevia pisteitä, esimerkiksi miljoona.
# Olkoon N tämä pisteiden kokonaismäärä. Jokaisesta neliön B sisään arvotusta pisteestä testataan vuorollaan,
# jääkö se myös yksikköympyrän A sisälle. Olkoon n ympyrän sisälle jäävien pisteiden kokonaismäärä.
# Nyt pätee n/N≈π/4, josta saadaan π≈4n/N.
# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä.
# Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle.
# (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on helppoa testata onko se yksikköympyrän A sisällä: riittää testata,
# toteuttaako piste epäyhtälön x^2+y^2<1.)

# Lets implement an algorithm for pii's (π) approximate value.
# Lets assume, that A is an Unit circle aka a circle, that centre point is in the origin and it's rain is 1.
# Around the circle will be drawn the most smallest square B in a way, that the circle A will be completely inside the square.
# Thus the squares corner point values are (-1, -1), (1, -1), (1,1) and (-1,1).
# If there would be made randomly generated a great amount of dots inside the circle,
# they will be hit also inside the circle approximately a value as big as the circle's area compared to the square's area hence πr^2/4,
# which (because the circle's rain is 1) will be simplified to π/4.
# Here we get a simple procedure to calculate the approximate value of the pii:
# Lets randomize inside of square B a great number of dots in different points, for example a million.
# Hence be N the total amount of the dots. Each dot that has been randomized inside the square B will be tested in turns,
# that will it be left also inside of the unit circle A. Hence be n the dots that will be left inside the circle.
# Now following applies: n/N≈π/4, where we will get π≈4n/N.

# Write a program, that asks the user the amount of dots that will be randomized and then it will execute the calculation for
# pii's approximate value by the given method given above ^.
# At the end, the program will print out pii's approximate value to the user.
# (Take in notice, that in each randomized point/dot (x,y) is easy to test if its inside the unit circle A:
# it will be enough to just test out the following false bulian? algebra? x^2+y^2<1.)
