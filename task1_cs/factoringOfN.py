import math
import time

e = 867512337310254731119
n = 1180592782282757817137
c = "MMCTNLAZNXEFUEN"


#Using Pollard's Rho algorithm for factorizing
#https://www.cs.colorado.edu/~srirams/courses/csci2824-spr14/pollardsRho.html
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


#Using the extendend euclid algorithm
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def euklid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = euklid((b % a), a)
    return g, (y - (b // a) * x), x


#Using RSA algorithm for generating private key
#http://doctrina.org/How-RSA-Works-With-Examples.html
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
    m = pow(c_zahl,d, N)

    m_string = ""

    #decode
    while (m > 0):
        m_string += chr((m % 26) + 65)
        m = m // 26

    return m_string

startTime = time.time()
message = decrypt(c, e, n)
print("Message:",message)
print("Runtime in seconds: " + str(time.time() - startTime))
