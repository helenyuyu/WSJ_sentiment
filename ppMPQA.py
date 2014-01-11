#!/usr/bin/env python
import json

pos = open('mpqa_positive.txt', 'w')
neg = open('mpqa_negative.txt', 'w')
prevpos = ""
prevneg = ""
with open('mpqa_raw.txt', 'r') as f:
    for line in f:
        temp = line.split()
        word = temp[2].split("=")[1]
        polarity = temp[5].split("=")[1]
        if ((polarity == "negative" or  polarity == "both") and word != prevneg):
            neg.write(word+"\n")
            prevneg = word
        if ((polarity == "positive" or  polarity == "both") and word != prevpos):
            pos.write(word+"\n")
            prevpos = word
pos.close()
neg.close()

