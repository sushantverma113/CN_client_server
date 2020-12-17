import pandas as pd
import numpy as np
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad , unpad

key = b'\xec\xee\xe2\xc9\x8f\xa1\x8d\xe2\xc9\xac\xdf\xe0\xe1\xa6\x96Y\xb4\x17\x1b\xecd}\x0e\x11\x0b\xc9\r7\xad\x84\x87\xc4'
iv = b'U\x99B\x1aR\xb99\xcf\x8c\x01\x878\xcf\xdb\x05f'

def decrypt_AES(array):
    new = []
    for i in range(0, len(array)):
        new.append([])
        for j in range(0, len(array[0])):
            new[i].append(0)
    for i in range(len(array)):
        for j in range(len(array[0])):
            cipher = AES.new(key, AES.MODE_CBC, iv)  # Setup cipher
            original_data = unpad(cipher.decrypt(array[i][j]), 16)
            new[i][j] = int(original_data)
    return (new)

def read_and_decrypt(filename):
    data = pd.read_csv(filename,header=None)
    data = np.array(data)
    new = []
    for i in range(0, len(data)):
        new.append([])
        for j in range(0, len(data[0])):
            new[i].append(int(data[i][j]).to_bytes(16,'big'))
    decrypted = decrypt_AES(new)
    return decrypted

def main():
    array = []
    array += read_and_decrypt('.\toReceive\part1.csv')
    # array += read_and_decrypt('.\toReceive\part2.csv')
    # array += read_and_decrypt('.\toReceive\part3.csv')
    df = pd.DataFrame(array)



    f = open('column_names.txt','r')

    col = []
    while True:
        x = f.readline()
        if len(x)==0:
            break
        col.append(x[:-1])

    df.columns = col
    df.to_csv('file.csv',index=False)