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

    #You search for the first collision and when that happens you also get lambda=length of circle
    #you get lampda because within the if the tortoise value is assigned the value of the hare
    #lampda is set to 0
    #each run that the hare does, the lampda is increased by 1
    #when there occurs a collision we know the length of the circle = lambda
    #(because tortoise value was not changed since then - lambda was increased by 1 each turn of hare)
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

    #We know the lenght of the circle=lambda
    #So we let the hare run until it reaches the lenght of the circle
    for i in range(0, lambdaVal):
        hareVal =  SHA2mod(CONST_PREFIX, hareVal)

    print('End of for')

    #Now we let the tortoise and hare run until we have the collision
    #(We know the lenght of the circle but not the tail mu - calculating the mu can be done here
    # but it is not needed here)
    #Collision will occur because they are the lenght of the circle apart from each other
    #Just a matter of time until the collusion occurs and then you also know the tail
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