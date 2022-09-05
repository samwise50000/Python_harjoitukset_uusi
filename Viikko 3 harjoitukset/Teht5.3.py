#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

n = int(input('Anna kokonaisluku. Ohjelma ilmoittaa, onko se alkuluku: '))

# Katsotaan, onko kokonaisluku suurempi kuin 1.

if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "ei ole alkuluku.")
			break
	else:
		print(n, "on alkuluku.")

# Jos numero on alempi kuin 1, se ei ole alkuluku.
else:
	print(n, "ei ole alkuluku.")