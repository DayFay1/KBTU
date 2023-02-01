N = int(input())
sum_a = 0
sum_n = 0

for i in range(N+1):
    sum_a += i
for i in range(N-1):
    sum_n += int(input())
print(sum_a - sum_n)