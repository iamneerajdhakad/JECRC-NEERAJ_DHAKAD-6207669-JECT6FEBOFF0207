
'''

dumps(): Encryption
loads(): Decryption


1. pickle, 
2. pickle,

'''

import pickle

file = open('temp.txt','ab+')

data = {
    'fulname': 'Neeraj Dhakad',
    'userid': 8736,
    'password':'*****'
}

print(f'Original Data: {data}')
print(f'Type of original Data: {type(data)}')
print()
enc_data = pickle.dumps(data)
# file.write(enc_data)
print(f'Original Encryped Data: {enc_data}')
print(f'Type of original Encryped Data: {type(enc_data)}')
print()
file.seek(0)
# enc_data = file.read()
# print(type(enc_data))

# ori_data = pickle.loads(enc_data)
# print(type(ori_data))
decp_data = pickle.loads(enc_data)
print(f'Original Decryped Data: {decp_data}')
print(f'Type of original Decryped Data: {type(decp_data)}')

file.close()
