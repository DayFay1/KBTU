n = int(input())*2
for i in range(1,n,2):
    print(int((n-i+1)/2)*' ' + i*'*' + int((n-i)/2)*' ')
    