
def decrypt(file_name, offset):

    file = open(file_name, 'rb')
    out = open('d_' + file_name[2:], 'wb')

    while byte := file.read(1):

        out.write(((byte[0] - offset) % 256).to_bytes(1, 'big'))
    
    file.close()
    out.close()


def main():

    inp = input("Input <file offset>: ").strip().split()

    try:
        decrypt(inp[0], int(inp[1]))

    except ValueError:
        print("Offset must be a number")


main()