

# Eingabe x = (a,k) und Loesung y = t

def V_sos(a,k,t):
    m = len(a)                                          # O(1)
    return k == sum(a[i] for i in range(m) if t[i])     # O(m)


a = [8,2,2,1,5]
k = 9

t = [1,0,0,1,0]
V_sos(a,k,t)

t = [0,1,1,1,0]
V_sos(a,k,t)

