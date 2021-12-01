
# iterativer Python-Interpreter wie Taschenrechner nutzbar
# primary prompt >>>
3 + 7
28 * 5

# Funktionedeklaration mit def
# Blockbildung durch Einruecktiefe
# Abschluss durch Leerzeile

def s(n):
    if n == 0:
        return 0 
    else:
        return s(n-1) + n   # rek. Aufruf

# Funkionsaufruf
s(10)


def sollwert(n):
    return (n*(n+1)) // 2   # ganzz. Division liefert Integer

# Vergleich
s(10) == sollwert(10)
s(11) == sollwert(10)


# Testfaelle 
for i in range(10):         # iterierbare Liste [0, 1, ..., 9]
    s(i) == sollwert(i)

for i in range(10):
    print(i, s(i), s(i) == sollwert(i))

