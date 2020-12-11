import pandas as pd
import numpy as np
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad , unpad

filename = 'data.csv'
key = b'\xec\xee\xe2\xc9\x8f\xa1\x8d\xe2\xc9\xac\xdf\xe0\xe1\xa6\x96Y\xb4\x17\x1b\xecd}\x0e\x11\x0b\xc9\r7\xad\x84\x87\xc4'
iv = b'U\x99B\x1aR\xb99\xcf\x8c\x01\x878\xcf\xdb\x05f'
data = pd.read_csv(filename,encoding='utf-8')


columns = list(data.columns)

data = np.array(data,dtype='str')

part1 = data[:int(len(data)/3)]
part2 = data[int(len(data)/3) : int(2*len(data)/3)]
part3 = data[int(2*len(data)/3) : ]

def encrypt_AES(array):
    new = []
    for i in range(0,len(array)):
        new.append([])
        for j in range(0,len(array[0])):
            new[i].append(0)
    for i in range(len(array)):
        for j in range(len(array[0])):
            cipher = AES.new(key, AES.MODE_CBC,iv)
            ciphered_data = cipher.encrypt(pad(bytes(array[i][j],encoding='utf-8'), 16))
            new[i][j] = int.from_bytes(ciphered_data,byteorder='big')
    return (new)


part1 = encrypt_AES(part1)
part2 = encrypt_AES(part2)
part3 = encrypt_AES(part3)


column_names_file = open('column_names.txt' , 'w')
for x in columns:
    column_names_file.write(x)
    column_names_file.write('\n')

pd.DataFrame(part1).to_csv("part1.csv",index=None,header=None)
pd.DataFrame(part2).to_csv("part2.csv",index=None,header=None)
pd.DataFrame(part3).to_csv("part3.csv",index=None,header=None)


