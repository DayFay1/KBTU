class Shape:
    def area():
        print(0)
class Rectangl(Shape):
    def __init__(self):
        self.len = input()
        self.wid = input()
    def area(self):
        print(int(self.len)*int(self.wid))

obj = Rectangl()
obj.area()