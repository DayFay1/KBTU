def square_generator(N):
    for i in range(1, N+1):
        yield i*i
# iterate over the generator and print the squares of numbers up to 5
for square in square_generator(5):
    print(square)

# convert the generator to a list and print it
squares_list = list(square_generator(10))
print(squares_list)