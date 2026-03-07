'''
Static Method:
A static method in Python is a method that belongs to a class's namespace but does not require access to instance-specific data (self) or class-specific data (cls). It functions like a regular, standalone function that happens to be logically grouped within a class for organizational purposes

It is neither related to object nor class.
For static method, there is no use self or cls.
“@staticmethod” decorator is used to create one static method.

'''
class Car:

    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

    # def __init__(self, air_bags, security, base_budget, varient, total_sale):
    #     self.air_bags = air_bags 
    #     self.security =security 
    #     self.base_budget = base_budget   
    #     self.varient = varient 
    #     self.total_sale = total_sale

    def display_properties(self):
        
        print({

            'wheelers':self.wheelers,
            'engine':self.engine,
            'base_speed': self.base_speed,
            'max_speed' : self.max_speed,
            'gears': self.gears,
            'air_bags':self.air_bags,
            'security':self.security,
            'base_budget': self.base_budget,
            'varient' : self.varient,
            'total_sale': self.total_sale
            })
        
    def update_base_speed(self, new_speed):
        self.base_speed = new_speed

    def update_max_speed(self, new_speed):
        self.max_speed = new_speed
    
    @classmethod
    def update_gear(cls, new_gears):
        cls.gears = new_gears
        print(f'No. of Gear: {cls.gears}')

    @staticmethod
    def greeting(name):
        print(f'Good Morning {name}')

msg=Car()
msg.greeting('World')
