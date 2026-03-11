
file = open('temp.txt','r')

print(file.readlines())
file.seek(0)
print(file.read())



file.close()