# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan
# takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.
fishLength = 37
fish = float(input("Anna kuhan mitta senttimetreinä: "))
if fish >= 37:
    print("Voit pitää kalan.")
elif fish < 37:
    print("Kuha on alimittainen. Kuha pitää laskea takaisin järveen. ")
    print(f"Kuhan pyyntimitta pitää olla yli 37cm. Kuhan pituudesta puuttuu {fishLength - fish:.2f} cm.")
