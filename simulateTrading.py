import csv
import json
import argparse

lexiconList = ['bingliu', 'inquirer', 'sentiwordnet', 'MPQA']
parser = argparse.ArgumentParser(description='Simulate trading, with decisions based on a user-provided lexicon and sentiment index threshold')
parser.add_argument("lexicon", help="lexicon to generate sentiment index",
                    type=str, choices = lexiconList)
parser.add_argument("threshold", help="sentiment index threshold",
                    type=float)
parser.add_argument("-v", "--verbose", help="display trading history", action="store_true")
parser.add_argument("-f", "--filter", help="use sentiment indices generated from filtered articles", action="store_true")
args = parser.parse_args()

lexicon = args.lexicon
threshold = args.threshold
if (args.verbose): verbose = True
else: verbose = False
if (args.filter): fLexicon = 'FilteredCounts_'+lexicon
else: fLexicon = 'RawCounts_'+lexicon
    
def djiaDate(date):
    dateComponents = date.split("-")
    return dateComponents[1] + " " + dateComponents[0] + ", 2008"

index = dict()
with open(fLexicon, 'r') as f:
     for line in f:
        data = json.loads(line)
        date = data['date']
        neg = float(data['neg'])
        pos = float(data['pos'])
        total = float(data['total'])
        index[date] = neg/total


indexSeries = [] #sentiment index
djia = [] #close djia
sp500 = [] #close sp500
indexSeries= []
with open ("djia_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:       
        if rownum != 0:
            date = djiaDate(row[0])
            indexSeries.append(index[date])
            djia.append(float(row[4]))
        rownum += 1


with open ("s&p500_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        if rownum != 0:
            sp500.append(float(row[4]))
        rownum += 1
        

moneyDJIA = 1
moneySP500 = 1
daysTraded = 0; 
i = 1
prevMoneyDJIA = 1
prevMoneySP500 = 1
while (i < len(djia)):
    if indexSeries[i] < threshold:
        #trade
        moneyDJIA = moneyDJIA/djia[i-1]*djia[i]
        moneySP500 = moneySP500/sp500[i-1]*sp500[i]
        if (verbose):
            print 'Day', i
            print 'DJIA:'
            print 'Money at beginning of day:', prevMoneyDJIA
            print 'Previous close:', djia[i-1]
            print 'Today\'s close:', djia[i]
            print 'Money at end of day:', moneyDJIA
            print 'S&P500:'
            print 'Money at beginning of day:', prevMoneySP500
            print 'Previous close:', sp500[i-1]
            print 'Today\'s close:', sp500[i]
            print 'Money at end of day:', moneySP500
            print '---------'
        daysTraded += 1
        prevMoneyDJIA = moneyDJIA
        prevMoneySP500 = moneySP500
    i+=1
print (str(daysTraded) + " days traded")
print ("DJIA: You have " + str(moneyDJIA) + " at the end of the year")
print ("SP500: You have " + str(moneySP500) + " at the end of the year")
