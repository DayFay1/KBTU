dep = int (input())
pl = int(input())
mn = int(input())
if pl < mn :
    print('It doesnt work!')
    pl = int(input())
    mn = int(input())
n = 0
cnt = 0
while n <= dep:
    n += pl
    if n < dep:
        n -= mn
    cnt += 1
print(f'{cnt} days')