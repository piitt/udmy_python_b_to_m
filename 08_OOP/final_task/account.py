class Account(object):
    """Класс Account банковский счет"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, depos_amount):
        """внести средства"""
        self.balance += depos_amount
        print('Внесение выпонено')

    def withdraw(self, wd_amount):
        """снять средства"""
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            print('Снятие выполнено')
        else:
            print('недостаточно средств')

    def __str__(self):
        return f'Владелец счета: {self.owner}\nБаланс счета: ${self.balance}'


acct1 = Account('Влад', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
acct1.withdraw(25)
print(acct1.balance)
acct1.withdraw(500)
