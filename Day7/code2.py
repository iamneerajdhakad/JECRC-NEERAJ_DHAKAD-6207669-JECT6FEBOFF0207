class Car:

    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

    def __init__(self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags = air_bags 
        self.security =security 
        self.base_budget = base_budget   
        self.varient = varient 
        self.total_sale = total_sale

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

TATA = Car(True,'Level 5','2L',12,100000)
print("BEFORE UPDATION ")
TATA.display_properties()
print()
print("AFTER UPDATION ")

TATA.update_base_speed('60')
TATA.update_max_speed('160')
TATA.display_properties()
mahindra = Car(True,'Level 4','4L',20,250000)
TATA.update_gear(5)
TATA.display_properties()
# TATA = Car() 
# TATA.engine = ['Petrol','Diesel','EV']
# TATA.air_bags = True ## oject properties
# TATA.no_of_air_bags = 4 ## oject properties
# TATA.base_budget = '2L'
# TATA.no_of_varient = 12


## constructor (__init__)

'''
class ClassName:
    properties
    
    def __init__(self,args1, args2, args3,.....argsn):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        ...
        self.argn = argn
'''

