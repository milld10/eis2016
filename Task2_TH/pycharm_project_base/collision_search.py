import hashlib
import time

CONST_PREFIX = '1430320143050014305291430751'
CONST_START_NUMBER = '2ac5'

def SHA2mod(prefix, message):
    colliding_message = prefix + message
    hash_object = hashlib.sha256(colliding_message.encode('utf-8'))
    #print(hash_object.hexdigest())
    chunkA = hash_object.hexdigest()[:8]
    chunkB = hash_object.hexdigest()[8:16]
    chunkC = hash_object.hexdigest()[16:24]
    chunkD = hash_object.hexdigest()[24:32]
    chunkE = hash_object.hexdigest()[32:40]
    chunkF = hash_object.hexdigest()[40:48]
    chunkG = hash_object.hexdigest()[48:56]
    chunkH = hash_object.hexdigest()[56:64]
    #print(chunkA, chunkB, chunkC, chunkD, chunkE, chunkF, chunkG, chunkH)

    XOR_ABCD_2 = int(chunkA, 16) ^ int(chunkB, 16) ^ int(chunkC, 16) ^ int(chunkD, 16)
    XOR_EFGH_1 = int(chunkE, 16) ^ int(chunkF, 16) ^ int(chunkG, 16) ^ int(chunkH, 16)
    XOR = (XOR_EFGH_1<<32)|XOR_ABCD_2
    #print("%x" % XOR_ABCD_2)
    #print("%x" % XOR_EFGH_1)
    #print("%x" % XOR)

    return "%x" % XOR
    #return "%x" % XOR_ABCD_2

def searchCollision():
    powerVal = 1
    lambdaVal = 1
    tortoiseVal = CONST_START_NUMBER
    hareVal = SHA2mod(CONST_PREFIX, CONST_START_NUMBER)

    while(hareVal != tortoiseVal):
        if(powerVal == lambdaVal):
            tortoiseVal = hareVal
            powerVal *= 2
            lambdaVal = 0
        hareVal = SHA2mod(CONST_PREFIX, hareVal)
        lambdaVal += 1

    print('End of first while')

    tortoiseVal = CONST_START_NUMBER
    tortoiseOldVal = CONST_START_NUMBER
    hareVal = CONST_START_NUMBER
    hareOldVal = CONST_START_NUMBER

    for i in range(0, lambdaVal):
        hareVal =  SHA2mod(CONST_PREFIX, hareVal)

    print('End of for')

    while(tortoiseVal != hareVal):
        tortoiseOldVal = tortoiseVal
        tortoiseVal =  SHA2mod(CONST_PREFIX, tortoiseVal)
        hareOldVal = hareVal
        hareVal = SHA2mod(CONST_PREFIX, hareVal)

    print('Collision was detected!!!')
    print('Collision with hash value ' + tortoiseVal)
    print('Normal value tortoise: ' + CONST_PREFIX + tortoiseOldVal)
    print('Normal value hare:     ' + CONST_PREFIX + hareOldVal)
    print('Control tortoise: ' + SHA2mod(CONST_PREFIX, tortoiseOldVal))
    print('Control hare:     ' + SHA2mod(CONST_PREFIX, hareOldVal))

startTime = time.time()
searchCollision()
print("Runtime in seconds: " + str(time.time() - startTime))
#print('Control tortoise: ' + SHA2mod(CONST_PREFIX, 'f14e6ba5'))
#print('Control hare:     ' + SHA2mod(CONST_PREFIX, '5d1b5e27'))