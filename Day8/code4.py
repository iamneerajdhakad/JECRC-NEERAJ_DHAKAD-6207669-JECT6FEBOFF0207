# Multilevel Inheritence: It is a type of inhertince in which the properties will be derived from one to another class by 
# considering more than one level

class Class_1:
    a = 'class_1'
class Class_2(Class_1):
    b = 'class_2'
    
class Class_3(Class_2):
    c = 'class_3'
    
class Class_4(Class_3):
    d = 'class_4'
    
class Class_5(Class_4):
    e = 'class_5'

child = Class_5()
print(child.a)
print(child.b)
print(child.c)
print(child.d)
print(child.e)
