'''
encapsulation: 
    1. It is used to provide security to the data(data means varible/properties/methods present inside class)

How to provide security to data?
    To provide security, we have to use access specifiers.
        1. public,
        2. protected(soft barrier (_)),
        3. private

Acess Specifier:
    It describes who can access class members(properties & methods).

'''

##example for public access specifiers

# class Temp:
#     a,b,*c,d = 'Hello'

#     def greeting(self):
#         print('Good Afternoon user!!')

# class C2(Temp):
#     pass


##protected 
# class Temp:
    
#     ##soft barrier(_) 
#     _a = 10 
#     _b = 'I Love PYTHON !'

# obj = Temp()
# print(obj._b)
# print(obj._a)

'''
1. By using Syntax,
2. get & set method,
3. by using @propery & decorater(setter)
'''
## By usig syntax
'''
obj_name/class_name._CN__propername/__method_name(accessing)
obj_name/class_name._CN__member_name = new_val(modifing)

'''
class Temp:
    
    
    __a = 100 #private variable

    def __status(self):
        print('Class name is Temp!!')

obj = Temp()
# print(obj.__status())

print(Temp._Temp__a)
obj._Temp__status()
Temp._Temp__a = '0123456789'
print(Temp._Temp__a)

def new_method():
    print('Changed')

obj._Temp__status  = new_method
obj._Temp__status()



# using get and set method

class Temp2:
    __a = 100

    def __status(self):
        print('Class name is Temp!!')
    
    def get(self):
        return self.__a
    def set(self,val):
        self.__a=val
        return self.__a
    
obj = Temp2()
print(obj.get())
obj.set(1)
print(obj.get())

print()


# By using @property decorator

class Temp3:
    __a = 100

    @property
    def get(self):
        print(self.__a)
    
    @get.setter
    def set(self,new_val):
        self.__a = new_val
    
obj = Temp3()

obj.get
obj.set = 10
obj.get


