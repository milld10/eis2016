import math

e = 867512337310254731119
n = 1180592782282757817137
c = "MMCTNLAZNXEFUEN"

def pseudorand(x, n):
    return (pow(x, 2)+1) % n

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
        return (b, 0, 1)
    else:
        g, x, y = euklid((b % a), a)
    return (g, y - (b // a) * x, x)


def generatePrivateKey(p, N, e):
    q = int(N/p)
    print(q)
    print(p)
    phi = (p - 1)*(q - 1)
    print("phi:",phi)
    print("e:",e)
    ggt, d, k = euklid(e, phi)
    print("d: ", d)
    return d

def decrypt(c, e, N):
    p = factorising(N)
    d = generatePrivateKey(p, N, e)
    print(d)
    m = ""
    for i in c:
        a = ord(i) - 65
        b = ((pow(a,d))% N) + 65
        m = m + chr(b)
    return m

message = decrypt(c, e, n)
print(message)
