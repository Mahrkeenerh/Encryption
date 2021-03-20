import numpy as np
import os


def decrypt(file_name, d, n):

    file = open(file_name, 'rb')

    temp = np.load(file).tolist()
    arr = temp[:-1]
    end = temp[-1]

    out_arr = []

    for i in arr[:-1]:

        temp = pow(i, d, n)

        for j in range(4):

            out_arr.append(int((temp % 256)).to_bytes(1, 'big'))
            temp = temp // 256

    temp = pow(arr[-1], d, n)

    for i in range(4 - end, 4):

        out_arr.append(int((temp % 256)).to_bytes(1, 'big'))
        temp = temp // 256

    file.close()
    file = open(file_name, 'wb')
    
    for i in out_arr:

        file.write(i)
    
    file.close()


def main():

    d = 666665802666906259
    n = 999998706000358093

    files = [f for f in os.listdir() if os.path.isfile(f)]

    for file in files:

        if 'rsa' not in file.lower():

            decrypt(file, d, n)


main()
