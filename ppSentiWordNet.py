#!/usr/bin/env python
import json
posWords = []
negWords = []
posFile = open('sentiwordnet_positive.txt', 'w')
negFile = open('sentiwordnet_negative.txt', 'w')
with open('sentiwordnet_raw.txt', 'r') as f:
    for line in f:
        if (line[0] != '#'):
            temp = line.split()
            posScore = float(temp[2])
            negScore = float(temp[3])
            if (posScore > 0):
                for token in temp:
                    temp2 = token.split('#')
                    if (len(temp2) == 2) :
                        posWords.append(temp2[0])
            if (negScore > 0):
                for token in temp:
                    temp2 = token.split('#')
                    if (len(temp2) == 2):
                        negWords.append(temp2[0])

prevpos = ""
prevneg = ""
posWords.sort()
for word in posWords:
    if word.find("_") == -1 and word != prevpos:        
        posFile.write(word+"\n")
        prevpos = word
posFile.close()        

negWords.sort()
for word in negWords:
    if word.find("_") == -1 and word != prevneg:
        negFile.write(word+"\n")
        prevneg = word
negFile.close()

