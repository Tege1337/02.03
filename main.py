lista = [2, 6, 4, 8, 1, 3, 9]

def osszegzes(szamok):
    osszeg = 0
    for x in szamok:
        osszeg += x
    return osszeg

sum = osszegzes(lista)
print(sum)