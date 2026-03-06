## Functions for String Data Type
'''
1.lower
2.upper
3.capitalize
4.title
5.strip
6.lstrip
7.rstrip
8.replace
9.index
10.split
11.join
12.startwith
13.endwith
14.isdigit
15.isalpha
16.islower
17.isupper

'''

s = 'pYTHON'

print(s) #pYTHON
print(s.upper()) #PYTHON
print(s.lower()) #python
print(s.capitalize()) #Python

s = '   JECRC   '

print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s = 'JECRC'
print(s.strip('C'))

print(s.replace('C','c'))

print(s.index('E'))
# print(s.index('e')) raise value error
print(s.find('E'))
print(s.find('Z')) # returns -1 when the index not found

s = "I LOVE PYTHON PROGRAMMING LANGUAGE"

print(s.split())
print(s.split('PYTHON'))

s = "I-LOVE-PYTHON-PROGRAMMING-LANGUAGE"
print(s.split('-'))
lsit_of_str=s.split('-')
print(lsit_of_str)
print('_'.join(lsit_of_str))

print(s.startswith(''))
print(s.endswith(''))

s='abc123'
print(s.isalpha())
print(s.isdigit())
s='ABc123'
print(s.islower())
print(s.isupper())


## Functions for List Data Type
'''
append
insert
extend
pop
remove
clear
sort
reverse
index
count

'''

s = ['a','b','c']
print(s)
s.append('d')
print(s)
s.insert(0,'d')
print(s)
s.extend([1,2,3])
print(s)

s.pop()
s.pop(1)
print(s)
s.remove(1)
print(s)

s.clear()
print(s)

s = ['a','b','c']
print(s)
s.sort(reverse=True)
print(s)
s.reverse()
print(s)

print(s.count(''))


## Functions for Tuple Data Type
'''

index
count

'''

## Functions for Set Data Type
'''

add
remove
discard
pop
clear
union

'''

s = [1,2,3,3,1.5]
st = set(s)
print(st)
st.add((1,2,3))
print(st)
st.remove(1)
print(st)
st.discard(10)
print(st)
st.pop()
print(st)

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1.union(s2)
s4 = s1.intersection(s2)
s5 = s1.difference(s2)
s6 = s2.difference(s1)
s7 = s1.symmetric_difference(s2)

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)


## Functions for Dictonary Data Type
'''

get
pop
popitem
keys
values
items


'''

d = {1:1,2:2,(1,2,3):[1,2,3]}
print(d[(1,2,3)])

user = {
    'username': 'user123',
    'password': '******',
    'location': 'IND'
}

print(user)
user.pop('username')
print(user.popitem())
print(user.update())
print(user)

