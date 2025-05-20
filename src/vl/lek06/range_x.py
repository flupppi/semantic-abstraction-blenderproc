

# verwendet bin_str(n) aus Uebung
from ueb.lek03.aufg15_bin_str import bin_str

# x besteht aus 100 Bits 1111...1
x = pow(2,100)-1

len(bin_str(x))  # n = |x| = 100

z = 0 
for i in range(0, x):
    z = z + 1

# z ist die ausgefuehrte Iterationszahl
# Abbruch mit crtl-c


def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y;
    else: 
        m = max(len(str(x)), len(str(y)))
        m2 = m//2
        
        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)
        
        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)
        
        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)
    
def karat(x,y):
    if len(str(x)) < 3 or len(str(y)) < 3:
        return x*y
    n = max(len(str(x)),len(str(y))) // 2
        
    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)
    
    z0 = karat(b,d)
    z1 = karat((a+b),(c+d))
    z2 = karat(a,c)
        
    return ((10**(2*n))*z2) + ((10**n)*(z1-z2-z0))+z0

karat(12, 12)

def multiply(x,y):
    if len