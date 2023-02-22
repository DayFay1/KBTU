class Parent1:
    def __init__(self,color1,number1):
        self.color1 = color1
        self.number1 = number1
        self.word1 = ''
    def printInfo1(self):
        print(f'Color:{self.color1}')
        print(f'Numbers:{self.number1}')
    def setWord1(self):
        self.word1 = input()
    def getWord1(self):
        return self.word1
class Parent2:
    def __init__(self,color2,number2):
        self.color2 = color2
        self.number2 = number2
        self.word2 = ''
    def printInfo2(self):
        print(f'Color:{self.color2}')
        print(f'Numbers:{self.number2}')
    def setWord2(self):
        self.word2 = input()
    def getWord2(self):
        return self.word2
    
class Baby(Parent1,Parent2):
    def __init__(self,color1,number1,color2,number2):
        Parent1.__init__(self,color1,number1)
        Parent2.__init__(self,color2,number2)
        self.color3 = self.color1 + '&' + self.color2
        self.number3 = self.number1 + self.number2
        self.word3 = ''
    def printInfo3(self):
        print(f'Color:{self.color3}')
        print(f'Numbers:{self.number3}')
    def getWord3(self):
        print(Parent1.getWord1(self) + Parent2.getWord2(self))

obj = Baby('Red','12','Blue','14')
obj.printInfo3()
obj.setWord1()
obj.setWord2()
obj.getWord3()
