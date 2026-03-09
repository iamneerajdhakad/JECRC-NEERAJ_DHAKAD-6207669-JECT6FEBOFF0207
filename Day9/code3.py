'''
Abstraction:
    Hiding the internal implementation and showing only functionality to the end user.

Abstract Method:
    If a method / function consists of only declaration not definition then it will be called as "Abstract Method"

Abstract Class:
    If a class consists of at least one abstract method, it will be called as "Abstract Class"

Concrete Class:
    It consists of zero(0) abstract method.

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod

class ATM(ABC): ## Abstract Class

    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SBI_ATM(ATM):

    def generate_pin(self):
        print('It is used to generate ATM Pin')

    def forget_pin(self):
        print('It is used to change ATM Pin')

    def check_balance(self):
        print('It is used to check balance')

    def withdraw(self):
        print('It is used to withdraw money from the ATM')

    def deposit(self):
        print('It is used to deposit money in ATM')


obj = SBI_ATM()

obj.check_balance()
obj.generate_pin()
obj.forget_pin()


