def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for square in squares(a, b):
    print(square)