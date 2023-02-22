def even_generator(n):
    for i in range(0, n+1, 2):
        yield str(i)

n = int(input("Enter a number: "))

even_numbers = even_generator(n)

print(",".join(even_numbers))