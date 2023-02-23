class ParentA:
    def __init__(self, a):
        self.a = a

    def print_a(self):
        print(f'a = {self.a}')

class ParentB:
    def __init__(self, b):
        self.b = b

    def print_b(self):
        print(f'b = {self.b}')

class Child(ParentA, ParentB):
    def __init__(self, a, b, c):
        super().__init__(a)  # Calls ParentA's __init__()
        super().__init__(b)  # Calls ParentB's __init__()
        self.c = c

    def print_c(self):
        print(f'c = {self.c}')