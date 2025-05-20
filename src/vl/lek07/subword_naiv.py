

# SUBWORD: kommt v in w vor?


def subword_naiv(w,v):
    m = len(w)              # Laenge
    k = len(v)
    d = 0                   # Rueckgabewert
    for i in range(m-k+1):  # pruefe an jeder moegl. Stelle in w
        if w[i:i+k] == v:   # ob v dort vorkommt
            d = 1
            break           # Schleife beenden
    return d


subword_naiv('abcdefg','ef')
subword_naiv('0123','')


# Laufzeit

# def subword_naiv(w,v):
#     m = len(w)              # O(1)
#     k = len(v)              # O(1)
#     d = 0                   # O(1)
#     for i in range(m-k+1):  # O(m)
#         if w[i:i+k] == v:   # O(i+k-i)=O(k)
#             d = 1           # O(1)
#             break          
#     return d                # O(1)
