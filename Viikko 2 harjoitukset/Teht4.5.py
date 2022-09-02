# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

username = "python"
password = "rules"
loginSucceeded = False
numberOfTries = 0

userNameInput = input('Anna Käyttäjätunnus: ')
passwordInput = input('Anna salasana: ')

numberOfTries += 1

if userNameInput == username and passwordInput == password:
    loginSucceeded = True

while loginSucceeded == False and numberOfTries < 5:
    userNameInput = input('Anna käyttäjätunnus ')
    passwordInput = input('Anna salasana: ')
    numberOfTries += 1

    if userNameInput == username and passwordInput == password:
        loginSucceeded = True

if loginSucceeded == True:
    print("Tervetuloa.")
else:
    print("Pääsy evätty.")
