
# Unterschiedliche Gruende für die Nichtdefiniertheit 
# der berechneten Funktion in WHILE-Programmen

def f(x):		# Endlosschleife		 	              				
    while (x != 0):			
        x = (x - 1)
    return x

f(3)
f(0)
f(-1)

def f(x):		# rekursive Aufrufe
    x = f((x+1))
    return x

f(2)


def f(x):		# nicht def. Variablen
    return z

f(1)