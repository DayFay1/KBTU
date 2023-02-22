class Person:
    def __init__(self,name,national):
        self.name = name
        self.s_name = 'None'
        self.national = national
    def printInfo(self):
        print(f'Name:{self.name}')
        print(f'Nationality:{self.national}')
    def setSurname(self):
        self.s_name = input()
    def getSurname(self):
        return self.s_name

class Student(Person):
    def printInfo(self,id = '123456'):
        print(f'Name:{self.name}')
        if self.s_name != 'None': print(f'Surname:{self.s_name}')
        print(f'Nationality:{self.national}')
        print(f'Id:',id)

obj = Student('Alex','USA')
obj.setSurname()
obj.printInfo()