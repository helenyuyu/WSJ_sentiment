#!/usr/bin/env python
import json
from bisect import bisect_left
import re

class RawCounts:
    def __init__(self, date, neg, pos, total):
        self.date = date
        self.neg = neg
        self.pos = pos
        self.total = total

#######################################################
# read in all WSJ articles
articlesByDate = dict()
with open('wsj_2008.txt', 'r') as f:
    for line in f:
        article = json.loads(line)
        date = article['date']
        if (date not in articlesByDate):
            articlesByDate[date] = ''    
        articlesByDate[date] += article['text'].lower() + "\n"

for date in articlesByDate.keys():
    article = articlesByDate[date]
    print date + ": " + str(len(article.split()))

#######################################################
lexiconList = ['bingliu', 'inquirer', 'sentiwordnet', 'MPQA'] 
for lexicon in lexiconList: 
    # import positive and negative words from lexicons
    posWords = []
    negWords = []
    posF = lexicon + '_positive.txt'
    negF = lexicon + '_negative.txt'
    # read positive words
    with open(posF, 'r') as f:
        for line in f:
            posWords.append(line.strip())
    # read negative words
    with open(negF, 'r') as f:
        for line in f:
            negWords.append(line.strip())
            
    posWords.sort()
    negWords.sort()
    
    # calculate raw counts for all days
    RawCountsByDate = dict()
    for date in articlesByDate.keys():
        daysArticles = articlesByDate[date];
        neg = 0
        pos = 0
        # calculate neg, pos, total for each day
        textTokens = re.findall(r"\w+(?:[-']\w+)*", daysArticles)
        total = len(textTokens)
        for token in textTokens:
            #print token
            i = bisect_left(posWords, token)
            if i != len(posWords) and posWords[i] == token:
                pos+=1
                #print token;
            i = bisect_left(negWords, token)
            if i != len(negWords) and negWords[i] == token:
                neg+=1
                #print token;
        RawCountsByDate[date] = RawCounts(date, neg, pos, total)
    
    # store data
    with open('RawCounts_' + lexicon, 'w') as f:
        for data in RawCountsByDate.values():
            json.dump(data.__dict__, f)
            f.write('\n')
            
    print(lexicon+ " done!!")