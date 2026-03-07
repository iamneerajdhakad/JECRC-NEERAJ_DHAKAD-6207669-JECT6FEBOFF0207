## Single Level
## we will have a single parent & child. also the properties will be derived onlt one time

class Parent:
    bank_balance = '54L'
    def desc(self):
        print('I am Parent Class') 

class Child(Parent):
    pass

obj = Child()
print(Child.bank_balance)
obj.desc()


