class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_detials(self):
        print('User Detials:')
        print("")
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'gender : {self.gender}')

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Account balace has been updated : ${self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insuficiant funds | Balance availible : ${self.balance}')
        else:
            self.balance = self.balance - amount
            print(f'Account balance has been updated : ${self.balance}')

    def view_balance(self):
        self.show_detials()
        print(f'Account balance : ${self.balance}')



b1 = Bank('zaki', 20, 'male')
b1.show_detials()
b1.deposit(100)
b1.withdraw(50)
b1.view_balance()