

# Grammatiken

def define_kfg_G_01(): 
    Sigma = {'0', '1'}  # Terminalsymbole 
    # Menge der Produktionsregeln
    P = {   ('S', ''),      # S -> epsilon               
            ('S', '0S1') }  # S -> 0S1
    N = {'S'}               # Menge der Nichtterminalsymbole    
    G = [Sigma, N, P, 'S']  # Grammatiktupel inkl Startsymbol als Liste
    return G


G_01 = define_kfg_G_01()
G_01


def define_kfg_G_pal(): 
    Sigma = {'a', 'b'}
    P = {   ('R', ''),      # R -> epsilon 
            ('R', 'a'),     # R -> a
            ('R', 'b'),     # R -> b
            ('R', 'aRa'),   # R -> aRa
            ('R', 'bRb') }  # S -> bRb
    N = {'R'}               
    G = [Sigma, N, P, 'R']
    return G


G_pal = define_kfg_G_pal()
G_pal


def define_kfg_G_Expr(): 
    Sigma = {'c', 'x', ')', '(', '-', '+'}
    P = {   ('S', 'x'),
            ('S', 'c'),
            ('S', '(S+S)'),
            ('S', '(S-S)') }
    N = {'S'}               
    G = [Sigma, N, P, 'S']
    return G


G_Expr = define_kfg_G_Expr()
G_Expr


