

from vl.lek08.delta_dach_dea import delta_dach_dea

# beliebigen DEA laufen lassen
def run_dea(A, w): 
    [Q, Sigma, delta, q0, F] = A                # unpacking in O(1)
    return delta_dach_dea(delta, q0, w) in F    # Aufruf in O(|w|), Test in O(1)           


# Verwendung
from vl.lek08.define_dea_A1 import define_dea_A1
A1 = define_dea_A1()
run_dea(A1,'1111000101')
