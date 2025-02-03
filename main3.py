lista = [61, 1, 61, 9, 2, 21, 43, 21, 681]

def harommal_oszthatok(szamok):
    darab = 0
    szam_list = []
    
    for x in szamok:
        if x % 3 == 0:
            darab += 1
            szam_list.append(x)

    return darab, szam_list

harommal_oszt = harommal_oszthatok(lista)
print(harommal_oszt)