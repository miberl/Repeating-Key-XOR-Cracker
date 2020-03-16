import math
import numpy


def isText(ASCIIValue):
    if (ASCIIValue >= 97 and ASCIIValue <= 122):
        return True
    else:
        return False


minKey = 1
maxKey = 20
hexstring = open("enc2.txt", "r").read()
byte = []

for i in range(0, len(hexstring), 2):
    byte.append(int(hexstring[i:i+2], 16))

keyguesses = []
notAscii = []
for i in range(minKey, maxKey):  # Keylength

    for j in range(0, i):                   #

        bestanswer = 0
        bestanswerpos = 0
        notbestanswer = 0
        ans = []
        for t in range(0, 255):
            count = 0
            notcount = 0
            for z in range(j, len(byte), i):
                if isText(byte[z] ^ t):
                    count += 1
                else:
                    notcount += 1
            if count > bestanswer:
                bestanswer = count
                bestanswerpos = t
                notbestanswer = notcount

        keyguesses.append(bestanswerpos)
        notAscii.append(notbestanswer)

key = minKey
finalmistakes = len(byte)
for i in range(minKey, maxKey):
    mistakes = 0
    for j in range(0, i):
        mistakes += notAscii.pop(0)


    mistakes = mistakes/i  # mistakes normalized
    if mistakes < finalmistakes:
        finalmistakes = mistakes
        key = i

print ("Keylength: ", key)
for i in range (minKey, key):
    for j in range (0,i):
        keyguesses.pop(0)
        
print ("Best key guess: ")
for i in range (0,key):
    guessedkey = keyguesses.pop(0)
    print hex(guessedkey),

# key = key / 2


# for i in range (0,key):
#     for j in range (0,255):
#         vowels=0
#         for z in range(i, len(byte), key):
#             if 