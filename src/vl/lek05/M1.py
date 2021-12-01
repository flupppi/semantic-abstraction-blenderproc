

# prodZ muss deklariert sein
from vl.lek04.prodZ import prodZ

# Idee: teste fuer in Frage kommende n
#       ob x=n*n
def M1(x):
    d = 0
    for n in range(0,(x+1)):
        z = prodZ(n,n)
        if (z == x):
            d = 1
    return d

#===============================================================================
# # M = {8, 2197, 10071}
# # Tipp ist Fallunterscheidung, da wir uns kein set anlegen dürfen.
# 
# def c_M(x): # charakteristische Funktion der Menge M
#     d = 0   # wenn nicht enthalten
#     if(((x==8) or (x==2197)) or (x==10071)): # Menge M als Fallunterscheidung
#         d = 1 # wenn enthalten
#     return d
# 
# for x in range(10072):  # Ausgabe der charakteristischen Funktion für die ersten 10071 Werte.
#     print(x, c_M(x))
#===============================================================================


def c_M(x):
    d = 0
    for n in range(0,(x+1)): # Rahmen des Entscheidungsproblem
        i = 0   # i = laufvariable (don't care ist ja nicht erlaubt)
        l = 1   # l = hilfswert zur berechnung des exponent
        for i in range(0,n):
            l = prodZ(l, 2)# Berechnung der Potenz 2**n
        z = l  
        if (z == x):  # entscheidung ob in der Menge enthalten.
            d = 1
    return d  

for x in range(101):
    print(x, c_M(x))


def prim(n):
    if (n > 0):
        if (n == 1):
            return 3
        primzahl = 3
        counter = 0
        while(counter != n):
            if(teil(primzahl) == 2): #Überprüfung der Zahl auf die Anzahl ihrer Teiler
                counter = (counter + 1)
            primzahl = (primzahl + 1)
def c_M(x):
    d=0
    for n in range(0,(x+1)):
        
    
for x in range(101):
    print(x, M1(x))
