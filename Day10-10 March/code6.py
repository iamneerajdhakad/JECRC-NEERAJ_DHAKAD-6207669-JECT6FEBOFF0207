
'''

dumps(): Encryption
loads(): Decryption


1. JSON, 
2. pickle,

'''

import json

file = open('temp.txt','a+')

data = {
    'fulname': 'Neeraj Dhakad',
    'userid': 8736,
    'password':'*****'
}

# print(f'Original Data: {data}')
# print(f'Type of original Data: {type(data)}')
# print()
enc_data = json.dumps(data)
file.write(enc_data)
# print(f'Original Encryped Data: {enc_data}')
# print(f'Type of original Encryped Data: {type(enc_data)}')
# print()
file.seek(0)
enc_data = file.read()
print(type(enc_data))

ori_data = json.loads(enc_data)
print(type(ori_data))
# decp_data = json.loads(enc_data)
# print(f'Original Decryped Data: {decp_data}')
# print(f'Type of original Decryped Data: {type(decp_data)}')

file.close()
