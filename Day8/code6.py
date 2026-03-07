# hierarchical : It is a type off inheritance in which the properties will be derived from single parent class
# to multiple child class.....

class Parent:
    gold = '2kg'
    silver = '10kg'
    no_of_flats = 12

class Youngest_Brother(Parent):
    name = 'Luffy'

class ElderBrother(Parent):
    name = 'Robin'

class Sister(Parent):
    name = 'Zoro'

print(Youngest_Brother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)


