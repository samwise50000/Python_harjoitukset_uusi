# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

# Write a program, that asks the user an username and a password.
# If either one or both are wrong, the username and password will be asked again.
# This will be continued until the login information are correct OR if the login info has been input wrong 5 times.
# In previous case the print will be: "Welcome" and the latter: "Access denied."
# (The username is "python" and the password "rules").

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
