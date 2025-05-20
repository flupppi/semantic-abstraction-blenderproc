

from vl.lek12.define_kfg import define_kfg_G_Expr

# Linksableitungsschritt 
def derive_left(alpha, p):
    (A, beta) = p       # p: A -> beta
    if A in alpha:
        # index of first occurence of A in alpha
        i = alpha.index(A)   
        return alpha[:i] + beta + alpha[i+1:]
    else: 
        return alpha


G_Expr = define_kfg_G_Expr()
[Sigma, N, P, S] = G_Expr

for alpha in {'S','(S-S)','(S+S)'}: # in diesen Satzformen
    for p in P:                     # mit diesen Regeln
        # =>_l ausfuehren
        print(alpha, p, derive_left(alpha, p))
