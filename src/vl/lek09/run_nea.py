

# Definition des NEA A
# beachten Sie den Unterschied bei delta

def define_nea_A(): 
    Q = {0, 1, 2, 3, 4} # Zustandsmenge
    Sigma = {'0', '1'}  # Alphabet    
    delta = {}              # leeres Dictionary
    delta[0,'0'] = {0,1}    # value = Menge (!) der Folgezustaende
    delta[0,'1'] = {0}    
    delta[1,'0'] = {2}    
    delta[1,'1'] = {2}
    delta[2,'0'] = {3}
    delta[2,'1'] = {3}
    delta[3,'0'] = {4}
    delta[3,'1'] = {4}
    delta[4,'0'] = set()    # leere Menge
    delta[4,'1'] = set()
    F = {4}             # Menge akz. Zustaende     
    A = [Q, Sigma, delta, 0, F]     # Automatentupel inkl Startzustand 
    return A

A = define_nea_A()


# erweiterte Ueberfuehrungsfunktion fuer NEAs
def delta_dach_nea(delta, q, w):
    R = {q}                 # (IA)
    for a in w:             # (IS)
        R = {q for p in R           # fuer alle p aus R_alt 
               for q in delta[p,a]} # die Mengen der Folgezustaende vereinigen    
    return R

# beliebigen NEA laufen lassen
def run_nea(A, w): 
    [Q, Sigma, delta, q0, F] = A                          # unpacking in O(1)
    return (delta_dach_nea(delta, q0, w) & F) != set()    # Test in O(#Q)           


# Verwendung
run_nea(A,'0111')
run_nea(A,'01110')



