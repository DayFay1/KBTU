sum = 0

while True:
    num = int(input("Enter a number between 1 and 10 (or 0 to exit): "))
    
    if num == 0:
        print("The program is finished, the final sum is:", sum)
        break
        
    elif num < 0 or num > 10:
        print("Sorry, if the number is not between 0 and 10 it's too hard for me.")
        
    else:
        sum += num
        print("The sum of all your numbers is:", sum)