
bil = 1000000000

arr = list([True for i in range(bil)])
file = open("ePrimes.txt", "w")
n = 0

for i in range(2, bil):

    if i % 100000 == 0:
        print(i)

    if not arr[i]:
        continue

    print(i, end=' ', file=file)
    n += 1

    if n % 100000 == 0:
        file.close()
        print(i)
        file = open("ePrimes.txt", "a")

    c = 2

    while c * i < bil:

        arr[c * i] = False
        c += 1
