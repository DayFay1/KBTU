n = int(input())
for i in range(1,n+2,2):
    print(int((n-i)/2)*' ' + i*'*' + int((n-i)/2)*' ')