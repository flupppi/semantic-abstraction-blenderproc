
from vl.lek13.cyk import cyk

# CNF-Grammatik fuer Expr
def define_kfg_G_Expr_CNF(): 
    Sigma = {')','(','x','c','-','+'}
    P = {   ('S', 'x'),   
            ('S', 'c'),
            ('A', '('),
            ('B', ')'),
            ('M', '-'),
            ('K', '+'),
            ('S', 'AU'), 
            ('U', 'SV'),
            ('V', 'MW'),
            ('W', 'SB'),
            ('S', 'AX'),
            ('X', 'SY'),
            ('Y', 'KZ'),
            ('Z', 'SB')  }
    N = {'S','A','B','M','K','U','V','W','X','Y','Z'}               
    G = [Sigma, N, P, 'S']
    return G


G = define_kfg_G_Expr_CNF()

cyk(G,'')
cyk(G,'(x)')
cyk(G,'(c-c)')
cyk(G,'((x+x)-((x-c)+(c-x)))')
cyk(G,'(x-)')
cyk(G,'(cc)')
cyk(G,'((((((c-c)-c)-c)-c)-c)-c)')



