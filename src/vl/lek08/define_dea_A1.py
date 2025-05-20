
# Definition des Automaten A1
# als Liste mit 5 Elementen

def define_dea_A1(): 
    Q = {0, 1, 2}       # Zustandsmenge
    Sigma = {'0', '1'}  # Alphabet    
    delta = {}          # leeres Dictionary
                        # Achtung: keys haben 2 Komponenten
    delta[0,'0'] = 1    # key = (Zustand, Eingabesymbol)
    delta[0,'1'] = 0    # value = naechster Zustand
    delta[1,'0'] = 1    
    delta[1,'1'] = 2
    delta[2,'0'] = 2
    delta[2,'1'] = 2
    F = {2}             # Menge akz. Zustaende     
    A = [Q, Sigma, delta, 0, F]     # Automatentupel inkl Startzustand 
    return A


A1 = define_dea_A1()


def dea_complement(A):
    Q = A[0]
    Sigma = A[1]
    delta = A[2]
    F = Q.difference(A[4])
    B=[Q, Sigma, delta, 0, F]
    return B

# Wichtig: nicht verwechseln
# Zustaenden 0,1,2 einerseits, und
# Eingabesymbole '0' und '1' andererseits