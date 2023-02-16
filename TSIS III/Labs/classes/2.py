class Shape:
    def area():
        print(0)
class Square(Shape):
    def __init__(self):
        self.len = input()
    def area(self):
        print(int(self.len)**2)

obj = Square()
obj.area()
