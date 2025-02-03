"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, 
ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
"""

lista = [61, 1, 61, 9, 2, 21, 43, 21, 681]

def paros_e(szamok):
    for x in szamok:
        if x % 2 == 0:
            return True

    return False

funkcio = paros_e(lista)
print(funkcio)