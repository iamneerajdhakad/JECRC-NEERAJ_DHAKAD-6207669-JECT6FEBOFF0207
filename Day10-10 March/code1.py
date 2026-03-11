import time
# exception handling : exception is an unauthorized event du to which it stops the flow of the execution of th program will be stopped after that it will never execute the further code

# syntax error cant be handled

# Pink/Purple : expection
# Red : Error
# Purple : Warning
'''
try: inside try block we will put problem statement (Block of code due to which we might get error)

except: inside this we put actual solution (Resolution for error prone code) of the error. Due to except bock we can prevent the unauthorised events(errors). 

finally: After getting error  or after resolution forcefully if we want to execute any particular block of code, we use finaaly block

else: It is an alternate of try block if we find any error inside try block interpretor will move forward towards else block . now inside else block if code is correct (output) and if code is incorrect (Error)

'''

'''
Exception Handling Approachs

--> Specific Exception Handling
--> Generic Exception Handling
--> Default Exception Handling

'''

'''

Specific Exception Handling

-- It we are aware of the error or, exception then we can go with "Specific".

try:
    probelm
    statement

except ErrorName:
    resolution/
    solution code


'''

# n1, n2 = 21, 0

# try:
#     result = n1/n2
# except ZeroDivisionError:
#     print("Please don't choose 0 as the second number")

# print('code after try except-01')
# print('code after try except-02')
# print('code after try except-03')


# try:
#     a, b, c = 1, 2
# except ValueError:
#     print("For performing MVC, no. of varibale and values should be equal")
# try:
#     print(a,b,c)
# except NameError:
#     print("Identifiers are not prenset in the memory")

# '''
# Generic Exception Handling
# -- It is a type of exception handling approach in which there is no need to pass any particular  exception class name. Instead of we can use parent class "Exception"

# -- Using "generic exception handling", we can't handle keyboard interruption
# '''

# try:
#     a, b, c = 1, 2
# except Exception:
#     print("For performing MVC, no. of varibale and values should be equal")
# try:
#     print(a,b,c)
# except Exception:
#     print("Identifiers are not prenset in the memory")

# code for KeyboardInterrupt
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop got stooped')

# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print('Loop got stooped')

'''

Default Exception: Have a kit kat, do nothing

'''

# try:
#     while True:
#         print(time.time())
# except:
#     print('Loop got stooped')

'''

raise --> it is a keyword, which help us to throw an error in between a program.

Exception Creation,

1. Custom Exception (raise)
2. user defined Exception (raise)
3. Assertion Exception (assert)

'''


'''
Custom Exception:
    1. we use pre built exception class according to our requirement.

    raise ValueError('message')

    ValueEorror: message
'''

# num = 17

# if num >= 18:
#     print('Eligible for Voting & Driving')

# else:
#     raise NameError('Age should be greater than or equal to 18!')


'''
-- User-defined Exception

    1. It is a type of exception in which we can create our own exception classess based upon our own requiement. we can also provide name to those classess based upon our own requirement. we can also provide name to those classess according the user cases
'''

class MyException(Exception):
    pass

# raise MyException('This is my exception class!!!')

# n1 , n2 = 18 , 0

# if n2==0:
#     raise MyException('Second num cant be zero!!')
# else:
#     print(n1/n2)


'''

Assertion Exception (assert)
-- Assertion exception can be created by using one keyword called "assert"

assert <condition>, print(ERROR)
print(output)

'''

s = input('Enter a String:')

assert s == s[::-1], 'Given String is not a palindrome!'
print(f'Given String {s} is a palindrome!')


