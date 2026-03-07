class MyDataType:
    def __init__(self,val):
        self.val = val

    def __add__(self,obj):
        return self.val+obj.val

    def __mul__(self, obj):
        return self.val*obj.val
    
obj1 = MyDataType(10)
obj2 = MyDataType(20)
print(obj1+obj2)
print(obj1*obj2)