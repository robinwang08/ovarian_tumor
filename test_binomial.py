import sys
from scipy.stats import binom_test

x = 0.44
n = 17
p = 0.44

print(binom_test(int(x * n), n, p))
