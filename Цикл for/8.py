N = int(input())
a = 1
c = 0
for i in range(1,N+1):
    for k in range(1,i+1):
        a *= k
    c += a
    a = 1
print(c)