n = 0
cnt = 0
while n <= 30:
    n += 7
    if n < 30:
        n -= 5
    cnt += 1
print(f'{cnt} days')
