'''
--operator overloading - its a phenomenon of making the operators to work on user-defined data types by invoking respective magic methods 

--magic method/ Dundar: It is a special type of method in which double underscores willbe there at starting & ending of the method's name 

-- exmaple: 
    1. __add__,
    2. __sub__,
    3. __mul__,
    4. __floordiv__,
    5. __truediv__,

-- if we don't use operator overloading then what will happen?
    For using the operators inside userdefined data type we have to use operator overloading

-- sytnax:
    class ClassName:
        def __init__(self,val):
            self.val = val
        def __add__(self, ano_obj):
            return self.val + ano_obj.val
    obj1 = ClassName(val1)
    obj2 = ClassName(val2)
    print(obj1 + obj2)
                
'''

class MyDT:
    def __init__(self,val):
        self.val = val

    def __add__(self, *args):
        sum=self.val
        for i in args:
            sum += i.val
        return MyDT(sum)

    def __sub__(self,ano_obj):
        return MyDT(self.val - ano_obj.val)
    
    def __mul__(self,ano_obj):
        return MyDT(self.val * ano_obj.val)
    
    def __floordiv__(self, ano_obj):
        return MyDT(self.val // ano_obj.val)
    
    def __truediv__(self, other):
        return MyDT(self.val / other.val)
    
    def __mod__(self, other):
        return MyDT(self.val % other.val)
    
    
    
    def __str__(self): ## when print(obj) python internally calls this method to display so if we override we can prevent print method to display memory address 
        return str(self.val)

# print(MyDT.add(MyDT(10), MyDT(30) , MyDT(10))) #addition
print(MyDT(10)+MyDT(30)+MyDT(10)*MyDT(2)) #subtraction
print(MyDT(10)-MyDT(30)+MyDT(10)+MyDT(20)*MyDT(2))
print(MyDT(10)//MyDT(3)) # floor divsion
print(MyDT(10)/MyDT(3)) # divsion
print(MyDT(10)%MyDT(3)) #modulus