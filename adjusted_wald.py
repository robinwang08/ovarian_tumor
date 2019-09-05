import sys

import math
def adjusted_wald(p, n, z=1.96):
    p_adj = (n * p + (z**2)/2)/(n+z**2)
    n_adj = n + z**2
    span = z * math.sqrt(p_adj*(1-p_adj)/n_adj)
    return max(0, p_adj - span), min(p_adj + span, 1.0)

print("({:.2f}-{:.2f})".format(*adjusted_wald(float(sys.argv[1]), float(sys.argv[2]))))
