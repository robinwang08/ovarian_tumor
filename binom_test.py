import sys
from scipy.stats import binom_test

x = float(sys.argv[1])
n = float(sys.argv[2])
p = float(sys.argv[3])

print(binom_test(int(x * n), n, p))
