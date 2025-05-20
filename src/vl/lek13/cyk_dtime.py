

# Laufzeit
# def cyk(G,w): 
#     [Sigma, N, P, S] = G              # O(1)
#      m = len(w)                       # O(1)
#     if m==0:                          # O(1)       
#         if (S,'') in P: return True   # O(1)
#         else: return False            # O(1)
#     T=[]                              # O(1)
#     for i in range(m):                # O(m)
#         l=[]                            # O(1)
#         for i in range(m):              # O(m)
#             l.append(set())               # O(1)
#         T.append(l)                     # O(1)
#     for i in range(m):                # O(m)
#        for A in N:                      # O(#N)
#             if (A,w[i]) in P:             # O(1)
#                 T[i][i] |= {A}            # O(1)
#     for k in range(1,m):              # O(m)
#         for i in range(0,m-k):          # O(m)
#             for j in range(i,i+k):        # O(m)  
#                 for (A,alpha) in P:         # O(#P)
#                     if len(alpha)==2          # O(1)
#                         and alpha[0] in T[i][j]      
#                         and alpha[1] in T[j+1][i+k]:
#                             T[i][i+k] |= {A}  # O(1)
#     return S in T[0][m-1]             # O(1)