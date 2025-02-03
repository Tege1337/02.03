"""
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét 
(0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
"""

def kerulet(*oldalak):
    kerulet_osszeg = 0

    if len(oldalak) == 1:
        kerulet_osszeg = float(oldalak[0]) * 4
    elif len(oldalak) == 2:
        kerulet_osszeg = 2 * (float(oldalak[0]) + float(oldalak[1]))
    elif len(oldalak) == 3:
        kerulet_osszeg = sum(float(oldal) for oldal in oldalak)
    elif len(oldalak) > 3:
        kerulet_osszeg = sum(float(oldal) for oldal in oldalak)

    return kerulet_osszeg

oldalak_hossz = input("Milyen hosszúak az oldalai a síkidomodnak? (Ha ugyanakkora csak egyszer írd be!) ").split()
oldalak_hossz = [float(oldal) for oldal in oldalak_hossz]

ossz = kerulet(*oldalak_hossz)
print(f"A síkidom kerülete: {ossz}")