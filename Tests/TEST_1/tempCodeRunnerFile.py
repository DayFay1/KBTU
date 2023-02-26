height = int(input())
character = input()

for i in range(1,height):
    if i == height - 1:
        print(  int((height-i))*' ' + ('/') + (((i-1)*2)-1)*'_' + ('\ '))
    elif i == 1:
        print(  int((height-1)) * ' ' + character) 
    else:
        print(  int((height-i))*' ' + ('/') + (((i-1)*2)-1)*' ' + ('\ '))