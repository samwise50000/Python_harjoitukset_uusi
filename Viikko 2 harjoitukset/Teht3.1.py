#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan
#takaisin järveen ilmoittaen samalla käyttäjälle,
#montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.
kuh_pyynt = 37
kuha = float(input("Anna kuhan mitta senttimetreinä: "))
if kuha >= 37:
    print("Voit pitää kalan.")
elif kuha < 37:
    print("Kuha on alimittainen. Kuha pitää laskea takaisin järveen. ")
    print(f"Kuhan pyyntimitta pitää olla yli 37cm. Kuhan pituudesta puuttuu {kuh_pyynt -kuha:.2f} cm.")