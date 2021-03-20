from threading import Thread
from time import sleep


def decryptBrute(file_name, offset):

    file = open(file_name, 'rb')
    out = open('d_' + str(offset) + '_' + file_name[2:], 'wb')

    while byte := file.read(1):

        out.write(((ord(byte) - offset) % 256).to_bytes(1, 'big'))

    file.close()
    out.close()


def main():

    inp = input("Input <file>: ")
    thread_arr = []

    try:
        for i in range(256):
            thread_arr.append(Thread(target=decryptBrute, args=(inp, i)).start())

    except ValueError:
        print("Offset must be a number")

    for i in range(256):

        try:

            thread_arr[i].join()
        except:
            
            continue


main()