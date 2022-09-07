def laskeKolmionAla(kanta, korkeus):
    A = (kanta * korkeus) / 2
    return A

ka = float(input("Anna kolmion kanta: "))
ko = float(input("Anna kolmion korkeus: "))
laskeKolmionAla(ka, ko)
pintaAla = laskeKolmionAla(ka, ko)
print(f"Kolmion ala on {pintaAla:.2f}")