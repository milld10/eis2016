import math

e = 867512337310254731119
n = 1180592782282757817137
c = "MMCTNLAZNXEFUEN"

def pseudorand(x, n):
    return ((pow(x, 2)+1) % n)

def factorising(n):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = pseudorand(x, n)
        y = pseudorand(pseudorand(y, n), n)
        d = math.gcd(abs(x-y), n)
    return d

def euklid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = euklid((b % a), a)
    return g, (y - (b // a) * x), x


def generatePrivateKey(p, N, e):
    q = int(N/p)
    print("q:",q)
    print("p:",p)
    phi = (p - 1)*(q - 1)
    print("phi:",phi)
    print("e:",e)
    ggt, d, k = euklid(e, phi)
    return d

def decrypt(c, e, N):
    p = factorising(N)
    d = generatePrivateKey(p, N, e)
    print("d:", d)
    counter = 0
    c_zahl = 0

    #encode
    for i in c:
        c_zahl += (ord(i) - 65) * pow(26, counter)
        counter += 1

    #decrypt
    m = (pow(c_zahl,d, N))

    #print(m)
    m_string = ""
    counter = 0
    m_rest = 0

    #decode
    while 1:
        if (m - m_rest) == 0:
            return m_string
        a = int(((m - m_rest) / pow(26, counter)) % 26)
        m_rest += (a * pow(26, counter))
        m_string += chr(a+65)
        counter += 1
        print(m_string)


message = decrypt(c, e, n)
print("Message:",message)
