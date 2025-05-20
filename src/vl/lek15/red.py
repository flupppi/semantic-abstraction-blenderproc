

# irgendein bereits bekannter Algo. fuer KS
def knapsack_algo(x):
    [s,v,S,k] = x
    # ...
    return 0

# Reduktionsfunktion
def f(x):
    [a,k] = x
    return [a,a,k,k]          # O(1)

# x in SOS gdw f(x) in KS
def sos_algo(x):
    return knapsack_algo(f(x))

#
x = [[8,2,2,1,5],9]
sos_algo(x)
