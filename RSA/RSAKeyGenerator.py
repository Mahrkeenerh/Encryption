
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def generatePublic(p, q):

    n = p * q
    fi = (p - 1) * (q - 1)
    e = 0

    no_arr = list(dict.fromkeys(prime_factors(fi))) + [p, q]

    for i in range(2, fi):

        clean = True

        for j in no_arr:
            
            if not i % j:
                clean = False
        
        if clean:

            e = i
            break

    return e, n, fi


# https://www.youtube.com/watch?v=Z8M2BTscoD4&ab_channel=AnthonyVance
def generatePrivate(e, fi):

    a1 = fi
    a2 = fi
    b1 = e
    b2 = 1

    while b1 != 1:

        div = a1 // b1
        c1 = (a1 - div * b1) % fi
        c2 = (a2 - div * b2) % fi

        a1 = b1
        a2 = b2
        b1 = c1
        b2 = c2

    return b2


def main():

    inp = input("Set primes <p q>: ").strip().split()

    try:

        int(inp[0])
        int(inp[1])
    
    except:

        print("p and q must be numbers")

    public = generatePublic(int(inp[0]), int(inp[1]))
    private = generatePrivate(public[0], public[2])

    print("E: {} N: {} D: {}".format(public[0], public[1], private))
    input()


main()
