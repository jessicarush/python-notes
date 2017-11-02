'''Rounding Issue with Floats and Solutions'''

# Floating point numbers are subject to rounding errors as they convert between
# binary and decimal. One solution is to use the decimal module that comes with
# python. The decimal module provides support for fast correctly-rounded
# decimal floating point arithmetic. It offers several advantages over the
# float datatype but will require some heavy investigation.

# The other method of dealing with this rounding error is to work strictly
# with integers instead of floats. This would mean multiplying by 100 and
# essential doing all calculations as pennies, then dividing by 100 to
# convert back to dollars for the final show_balance.

# -----------------------------------------------------------------------------
# Example 1: floats
# -----------------------------------------------------------------------------

class Account1():

    def __init__(self, name: str, opening_balance: float=0.0):
        self.name = name
        self._balance = opening_balance
        print('Account created for {}'.format(self.name))
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print('{} deposited'.format(amount))
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print('{} withdrawn'.format(amount))
            return amount
        else:
            print('Amount must be greater than 0 and not exceed balance')
            return 0.0

    def show_balance(self):
        print('Balance on account {} is {}'.format(self.name, self._balance))

# testing:
if __name__ == '__main__':
    rick = Account1('Rick')
    rick.deposit(100.10)
    rick.deposit(499.10)
    rick.deposit(55.10)
    rick.withdraw(80.00)
    rick.show_balance()

# -----------------------------------------------------------------------------
# Example 2: decimal module
# -----------------------------------------------------------------------------

from decimal import *

class Account2():

    # class constant, accessible without creating an instance
    _qb = Decimal('0.00')

    def __init__(self, name, opening_balance=0.0):
        self.name = name
        self._balance = Decimal(opening_balance).quantize(Account2._qb)
        print("Account created for {}. ".format(self.name))
        self.show_balance()

    def deposit(self, amount):
        decimal_amount = Decimal(amount).quantize(Account2._qb)
        if decimal_amount > Account2._qb:
            self._balance = self._balance + decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._balance

    def withdraw(self, amount):
        decimal_amount = Decimal(amount).quantize(Account2._qb)
        if Account2._qb < decimal_amount <= self._balance:
            self._balance = self._balance - decimal_amount
            print("{} withdrawn".format(decimal_amount))
            return decimal_amount
        else:
            print('Amount must be greater than 0 and not exceed balance')
            return Account2._qb

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))

#testing:
if __name__ == '__main__':
    rick = Account2('Rick')
    rick.deposit(100.10)
    rick.deposit(499.10)
    rick.deposit(55.10)
    rick.withdraw(80.00)
    rick.show_balance()

# -----------------------------------------------------------------------------
# Example 3: use integers
# -----------------------------------------------------------------------------

class Account3():

    def __init__(self, name: str, opening_balance: int=0):
        self.name = name
        self._balance = opening_balance
        print('Account created for {}'.format(self.name))
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print('{:.2f} deposited'.format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print('{:.2f} withdrawn'.format(amount / 100))
            return amount / 100
        else:
            print('Amount must be greater than 0 and not exceed balance')
            return 0.0

    def show_balance(self):
        print('Balance on account {} is {:.2f}'.format(
               self.name, self._balance / 100))

# testing:
if __name__ == '__main__':
    rick = Account3('Rick')
    rick.deposit(10010)
    rick.deposit(49910)
    rick.deposit(5510)
    rick.withdraw(8000)
    rick.show_balance()
