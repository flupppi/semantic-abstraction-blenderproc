'''
Created on 16.10.2020

@author: Felix Kalchschmid
'''
# Meine Loesung für Aufgabe 2.1


# rekursive funktion die g berechnet
# für werte größer gleich 1
def g(m):
    if m==1: return 1         # g(1) ohne Vorgaenger
    elif m>=2: return g(m-1)+m**3

# sollwert funktion zum testen der funktion g
def sollwert(n):
    if n>=1:
        i = ((n*(n+1))/2)**2
        return i
    
# Ausgabe zum Vergleichen der ergebnisse von g und sollwert
for i in range(1,20):     # untere Grenze 0
    print(g(i), sollwert(i),sollwert(i)==g(i))
    
