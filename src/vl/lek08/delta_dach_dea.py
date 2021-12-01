
from vl.lek08.define_dea_A1 import define_dea_A1


# unpacking: den Komponenten von A1 Namen geben
A1 = define_dea_A1()
[Q, Sigma, delta, q0, F] = A1
Q
delta


# erweiterte Ueberfuehrungsfunktion fuer DEAs
def delta_dach_dea(delta, q, w): 
    for a in w:             # fuer jedes Eingabesymbol
        q = delta[q, a]     # bestimme Folgezustand
    return q

# delta ist Argument, d.h. die Fkt ist fuer jeden DEA nutzbar

delta_dach_dea(delta, 0, '1100')    # liefert Zustand 1
delta_dach_dea(delta, 1, '001')     # liefert Zustand 2
delta_dach_dea(delta, 2, '')        # liefert Zustand 2 

# Laufzeit ist O(|w|)
#
# def delta_dach_dea(delta, q, w): 
#     for a in w:             # O(|w|)
#         q = delta[q, a]     # O(1)
#     return q                # O(1)


# auch rekursive Implementierung analog ind.Def. ist moeglich:
def delta_dach_dea_rek(delta, q, w): 
    if w == '': return q                                        # (IA)
    return delta[delta_dach_dea_rek(delta, q, w[:-1]), w[-1]]   # (IS)

