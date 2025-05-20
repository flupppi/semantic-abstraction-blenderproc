
from vl.lek04.prodZ import prodZ

def divZ(x,y):
    if (y != 0):    # nicht def. Rueckgabe, falls y=0
        if (y < 0):
            y = (0 - y)     # neg. Vorzeichen von y
            x = (0 - x)     # auf x uebertragen
        z = 0
        if (x < 0):         # z = min(0,x)
            z = x
                            # hier gilt y>0 und y*z <= x
        while (prodZ(y,z) <= x):    # suche groesstes z 
            z = (z + 1)             # mit y*z<=x
        z = (z - 1)         # zu weit gezaehlt
    return z

divZ(11,5)
divZ(-11,5)
divZ(11,-5)