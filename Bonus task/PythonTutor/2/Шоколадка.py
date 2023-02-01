n = int(input())
m = int(input())
k = int(input())
if (k%n == 0 or k%m == 0) and m*n > k:
    print("YES")
else:
    print("NO")