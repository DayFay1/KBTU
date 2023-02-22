n = int(input())
tick = 1
for i in range(2,n):
    if n%i == 0:
        print('No because:',str(int(n/i)) + ' * ' + str(i) + ' = ' + str(n) )
        tick = 0
        break
else:
    tick == 1
    print('Its prime')