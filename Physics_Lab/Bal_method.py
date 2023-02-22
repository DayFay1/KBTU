import math
M = 181.5
m = 1.84
L1 = float(input())
L = float(input())
t = float(input())
t1 = float (input())
N = 10
T = t/N
T1 = t1/N
fi = math.radians(38)
V = (4*math.pi*M*L1**2*fi)/(m*L*(T**2-T1**2))
print(f'V = {V}')
