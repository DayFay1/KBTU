a = int(input())
b = int(input())
c = int(input())
cnt = 0
if a == b and b == c:
    cnt = 3
elif a == b or a == c or b == c:
    cnt = 2
print(cnt)