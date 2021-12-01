
# Beispiele fuer Funktionsdeklarationen

def f(x,y):                
    z = 0                                  
    while (x > 0):            
        z = (z + y)
        x = (x - 1)
    return z

f(3,4)
f(3,-4)
f(-3,4)

def g(x,y):  
    for i in range(x,y):
        j = (j + i)
        z = (j + j)
    return z

g(2,5)
g(5,2)

def h(x,y):   
    return (x + y)

h(1,2)
h(-1,2)