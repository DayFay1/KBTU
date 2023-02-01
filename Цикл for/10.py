s = ""
N = int(input())
for i in range(1,N+1):
    for k in range(1,i+1):
        s += str(k)
    print(s)
    s = ""