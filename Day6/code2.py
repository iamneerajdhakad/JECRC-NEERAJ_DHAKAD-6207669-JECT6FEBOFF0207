## Packing 

## create a function which can take n no of int or float numbers and returns only tier addition.
'''
def add_nums(*args):
    print(args,type(args))
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add_nums) # accessing the function
print(add_nums(1,2,3,4,4.5,2.3)) # function calling 


def add_nums(*args):
    args = list(args)
    print(args,type(args))
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add_nums) # accessing the function
print(add_nums(1,2,3,4,4.5,2.3)) # function calling 

## Create a function which will take n no of inputs from the user adn return the sum of only int and floating point number. 

def add_nums(*args):
    # args = str(args)
    sum = 0
    for i in args:
        if type(i) in [int,float]:
            sum += i
    return sum

print(add_nums()) # function calling

'''
'''
def fun_name(**kwargs):
    pass

fun_name(k1=v1,k2=v2,....,kn=vn)

All the keys names should a string but con't use quotes.
'''

def print_details(**kwargs):
    return kwargs

print(
    print_details(username='user123',password='******',logged_in_devices=['Adriod','Windows','Linux'])
)


def add_nums(*args):
    # args = str(args)
    sum = 0
    for i in args:
        if type(i) in [int,float]:
            sum += i
    return sum

print(add_nums(*eval(input()))) # function calling