class Str:
    def __init__(self):
        self.str = ''
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
obj = Str()
obj.getString()
obj.printString()