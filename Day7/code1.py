class Car:

    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

TATA = Car() 
TATA.air_bags = True ## oject properties
TATA.security = 'level 5' ## oject properties

print('Properties for TATA ------')
print(f'No of Wheelers: {TATA.wheelers}')
print(f'No of Engine: {TATA.engine}')
print(f'No of Max_speed: {TATA.max_speed}')
print(f'No of Gears: {TATA.gears}')
print(f'No of air_bags: {TATA.air_bags}')
print(f'No of security: {TATA.security}')
print()
mahindra = Car() 
print(f'No of Wheelers: {mahindra.wheelers}')
print(f'No of Engine: {mahindra.engine}')
print(f'No of Max_speed: {mahindra.max_speed}')
print(f'No of Gears: {mahindra.gears}')
print()
suzuki = Car()
print(f'No of Wheelers: {suzuki.wheelers}')
print(f'No of Engine: {suzuki.engine}')
print(f'No of Max_speed: {suzuki.max_speed}')
print(f'No of Gears: {suzuki.gears}')
print()
toyota = Car()
print(f'No of Wheelers: {toyota.wheelers}')
print(f'No of Engine: {toyota.engine}')
print(f'No of Max_speed: {toyota.max_speed}')
print(f'No of Gears: {toyota.gears}')

