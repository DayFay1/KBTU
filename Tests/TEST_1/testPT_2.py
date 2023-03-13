import math
from decimal import Decimal

n = math.ceil(1150 * 1.15)
p = Decimal('0.95')
k = 1

while True:
    cumulative_prob = sum((p**i) * ((1-p)**(n-i)) * math.comb(n, i) for i in range(k, n+1))
    if cumulative_prob >= Decimal('0.95'):
        break
    k += 1

print(k)


