## constructor chaining : calling parent class constructor from inside child class constructor is known as Constructor chaining
class Parent:
    bank_balance = '54L'

    def __init__(self,members):
        self.members = members

    def desc(self):
        print('I am Parent Class') 

class Child(Parent):
    def __init__(self,child_name ,*args):
        super().__init__(args)
        self.child_name=child_name

    def display(self): ## Method chaining
        super().desc()


obj = Child('child','Mom','Dad')
print(obj.members,obj.child_name)
obj.display()


