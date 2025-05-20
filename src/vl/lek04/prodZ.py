
def prodZ(x,y):     # Funktionsdeklaration
    z = 0           # Initialisierung
    if (x < 0):   
        x = (0 - x)         # neg. Vorz. von x entfernen
        y = (0 - y)         # und auf y uebertragen
    for i in range(0,x):    # x Durchlaeufe
            z = (z + y)     # y wird x-mal zu z addiert
    return z

#prodZ(-3,12)