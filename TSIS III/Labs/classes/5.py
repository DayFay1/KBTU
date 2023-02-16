class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.dep = 0
    def deposit(self):
        mny = input("Как много хотите вложить?")
        if(mny > self.balance):print("Вы превышаете баланс")
        else:
            self.dep = mny
            print("Операция прошла успешно")
    def withdraw(self):
        mny = input("Как много хотите вложить?")
        if(mny > self.balance):
            print("Вы превышаете баланс")
        elif(self.balance + self.dep >= mny):
            "Деньги для снятия были взяты с депозита(Мы плохой банк)"
        else:
            print("Операция прошла успешно")