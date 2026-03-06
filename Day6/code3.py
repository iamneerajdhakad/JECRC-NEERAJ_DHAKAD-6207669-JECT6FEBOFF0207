# Create a function which will return a list of prime numbers. 
# Please make sure that user can pass n of inputs for checking a number is prime or not

def isPrime(num):

    if num <= 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if(i*i==num):
                return False
            if(num%i==0):
                return False

        return True


def find_prime_nums(*args):
    prime=[]

    for i in args:
        if isPrime(i):
            prime.append(i)

    return prime

print(find_prime_nums(*eval(input("Enter a list of numbers"))))


