# Hybrid Inheritence : It is a mixture of more than one type of inheritence

class Class1:
    pass
class Class2(Class1):
    pass
class Class3(Class2):
    pass
class Class4(Class2):
    pass
class Class5(Class2):
    pass
class Class6(Class3,Class4,Class5):
    pass