'''
lambda(Anonymous Function):
    1. Lamba is a keyword which is used to create anonymous function.
    2.. For calling the lambda function, we can store the address of lambda inside a variable . bt invoking the var_name we can call the function
'''

## lambda args: <exp>

# result = lambda a,b : a+b
# print(result)
# print(result(1,3))

# (lambda a,b : print(a+b))(int(input("First Num: ")),int(input("Second Num: ")))




# WAP to find the square of a number if it is even
# if not(num % 2):
#     print( num**2)

num = int(input())
# result = lambda num : print(num ** 2) if num % 2==0 else None 

# if num > 0:
#     print('POS')
# else:
#     if num < 0:
#         print('Neg')
#     else:
#         print('Zero')

result = lambda num : print('POS') if num > 0 else print('Neg') if num < 0 else print('Zero')
result(num)




