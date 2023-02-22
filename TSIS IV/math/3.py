import math

n = int(input("Enter the number of sides of the regular polygon: "))
s = float(input("Enter the length of each side of the regular polygon: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the regular polygon is {area:.2f}.")