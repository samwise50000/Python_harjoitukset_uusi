# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

year = int(input('Anna vuosiluku: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Vuosiluku on karkausvuosi.')
        else:
            print('Vuosiluku ei ole karkausvuosi.')
    else:
        print('Vuosiluku on karkausvuosi.')
else:
    print('Vuosiluku ei ole karkausvuosi.')

