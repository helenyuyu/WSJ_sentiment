#!/usr/bin/env python
import json
import re

count = 0
articlesByDate = dict()
with open('wsj_2008.txt', 'r') as f:
    for line in f:
        article = json.loads(line)
        if (article['date'] == "Jan 2, 2008") :
            text = article['text'].lower()
            tokens = re.findall(r"\w+(?:[-']\w+)*", text)
            #tokens = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S", text)
            for token in tokens:
                #print token
                count+= 1
    print count



