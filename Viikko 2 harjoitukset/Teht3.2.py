# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

cabinClass = input("Anna laivan hyttiluokka. Kelvolliset hyttiluokat ovat: LUX, A, B, C: ")

if cabinClass == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif cabinClass == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif cabinClass == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif cabinClass == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')
