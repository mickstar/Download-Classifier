"""
This a utility class to generate common tokens from a given set of files.
"""
from heapq import nlargest
import os

outputToFile = False

nTokens = 1000

tokens = {}

dataset = os.listdir ("/media/HDD/Movies")
n = 3
for item in dataset:
    tokensForItem = (item.upper()
                        .replace(".", " ")
                        .replace("-", " ")
                        .split (" "))
    for token in tokensForItem:
        if token not in tokens:
            tokens[token] = 0
        tokens[token] += 1


nL = nlargest (1000, tokens.items(), key=lambda sc : sc[1])

print ([token for token,score in nL])

if (outputToFile):
    file = open ("movieTokenData.py", "w")
    file.write ("movieTokens = %s" %(str([token for token,score in nL])))
    file.close()
