s = input('I said hello,do you have to something to say me? ')
n = 1
while s != 'Hello':
    n += 1
    if n < 4:
        s = input('I said hello,do you have to something to say me? ')
    elif n >= 4 and n < 7:
        s = input('You have to say hello to me! ')
    elif n >= 7:
        s = input('I SAID HELLO,ANSWER HELLO!!! ')
else:
    print('Hello,how are you?')