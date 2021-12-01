

# G ist KFG in CNF
# entscheidet, ob w in L(G)
def cyk(G,w): 
    [Sigma, N, P, S] = G
    m = len(w)
    # Fall w=eps behandeln
    if m==0:                
        if (S,'') in P: return True
        else: return False
    # m x m Matrix T mit set() initialisieren
    # als Liste von Listen
    T=[]
    for i in range(m):
        l=[]
        for i in range(m):
            l.append(set())
        T.append(l)
    # (IA) k=0
    for i in range(m):
        for A in N:
            if (A,w[i]) in P:
                T[i][i] |= {A}
    # (IS) k >= 1
    for k in range(1,m):                # bestimme 
        for i in range(0,m-k):          # T[i][i+k]
            for j in range(i,i+k):        
                for (A,alpha) in P:     
                    if len(alpha)==2 \
                        and alpha[0] in T[i][j] \
                        and alpha[1] in T[j+1][i+k]:
                            T[i][i+k] |= {A}
    return S in T[0][m-1]


# Test: CNF-Grammatik aus Bsp 13.3
# aber fuer alle NTs nur ein Zeichen:
# B_a=A, B_b=B, A_1=U, A_2=V, A_3=W, A_4=X
def define_kfg_G(): 
    Sigma = {'a', 'b'}
    P = {   ('S', ''),   
            ('S', 'a'),
            ('S', 'b'),
            ('S', 'AA'),
            ('S', 'BB'),
            ('S', 'AU'),
            ('S', 'BV'), 
            ('R', 'a'),
            ('R', 'b'),
            ('R', 'AA'),
            ('R', 'BB'),
            ('R', 'AW'),
            ('R', 'BX'),
            ('U', 'RA'),
            ('V', 'RB'),
            ('W', 'RA'),
            ('X', 'RB'),
            ('A', 'a'),
            ('B', 'b')    }
    N = {'S','R','A','B','U','V','W','X'}               
    G = [Sigma, N, P, 'S']
    return G


G = define_kfg_G()
cyk(G,'')
cyk(G,'baaba')
cyk(G,'aaabbaaa')
# cyk(G,'a'*150)
# cyk(G,'a'*150+'b')

