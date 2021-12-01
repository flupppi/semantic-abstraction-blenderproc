
# verwendet Verifikationsalgorithmus fuer Loesungen
from vl.lek14.V_sos import V_sos

# geeigneten Iterator waehlen
from itertools import product
def sos_exhaustive(a,k):            
    m = len(a)                                      # O(1)
    for t in product((0,1),repeat=m):               # alle 0-1-Tupel der Laenge m,  O(2^m)
        if V_sos(a,k,t):                            # Loesung zulaessig? O(m)
            print({i for i in range(m) if t[i]})    # Ausgabe Indexmenge
            return 1                                # O(1)
    return 0                                        # O(1)

# Bsp
sos_exhaustive([8,2,2,1,5],9)
