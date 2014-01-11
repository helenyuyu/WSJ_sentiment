#!/usr/bin/env python
import json

newfile = open('inquirer_positive.txt', 'w')
prev = ""
with open('inquirer_positive_raw.txt', 'r') as f:
    for line in f:
        l = line.lower().strip('\n').split("#")
        word = l[0]
        if (word != prev): 
            newfile.write(word+"\n")
            prev = word
newfile.close()

newfile = open('inquirer_negative.txt', 'w')
prev = ""
with open('inquirer_negative_raw.txt', 'r') as f:
    for line in f:
        l = line.lower().strip('\n').split("#")
        word = l[0]
        if (word != prev): 
            newfile.write(word+"\n")
            prev = word
newfile.close()