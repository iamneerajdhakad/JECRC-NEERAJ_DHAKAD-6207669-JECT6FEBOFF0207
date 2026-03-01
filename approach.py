n1 = int(input())
n2 = int(input())

result = n1 + n2
print(result)

class AddTwoNums:
    @staticmethod
    def result(n1,n2):
        return(n1+n2)

print(AddTwoNums.result(n1,n2))    

(lambda a, b: print(a + b))(n1, n2)