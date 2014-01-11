import csv
import json


def djiaDate(date):
    dateComponents = date.split("-")
    return dateComponents[1] + " " + dateComponents[0] + ", 2008"
def vixDate(date):
    dateComponents = date.split("/")
    if dateComponents[0] == 1: month = Jan
    if dateComponents[0] == 2: month = Feb
    if dateComponents[0] == 3: month = Mar
    if dateComponents[0] == 4: month = Apr
    if dateComponents[0] == 5: month = May
    if dateComponents[0] == 6: month = Jun
    if dateComponents[0] == 7: month = Jul
    if dateComponents[0] == 8: month = Aug
    if dateComponents[0] == 9: month = Sep
    if dateComponents[0] == 10: month = Oct
    if dateComponents[0] == 11: month = Nov
    if dateComponents[0] == 12: month = Dec
    return month + " " + dateComponents[1] + ", 2008"

#import raw counts
lexiconList = ['bingliu', 'inquirer', 'sentiwordnet', 'MPQA']

index = dict()
for lexicon in lexiconList:
    index[lexicon] = dict()
    with open('FilteredCounts_'+lexicon, 'r') as f:
         for line in f:
            data = json.loads(line)
            date = data['date']
            neg = float(data['neg'])
            pos = float(data['pos'])
            total = float(data['total'])
            index[lexicon][date] = neg/total



fDJIA = open("timeseries_DJIA", "w")
fLexicon = open("timeseries_Lexicon", "w")
with open ("djia_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:       
        if rownum == 0:
            for lexicon in lexiconList:
                fLexicon.write(lexicon + " ")
            fLexicon.write("\n")
        elif rownum > 1:
            date = djiaDate(row[0])
            for lexicon in lexiconList:
                fLexicon.write(str(index[lexicon][date]) + " ")
            fLexicon.write("\n")
            fDJIA.write(row[4] + "\n")
        rownum += 1

fLexicon.close()
fDJIA.close()

fVIX = open("timeseries_VIX", "w")
with open ("vix_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        if rownum > 1:
            fVIX.write(row[4] + "\n")
        rownum += 1
fVIX.close()

fSP500 = open("timeseries_s&p500", "w")
with open ("s&p500_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        if rownum > 1:
            fSP500.write(row[4] + "\n")
        rownum += 1

fSP500.close()

fVolume = open("timeseries_volume", "w")
with open ("volume_2008.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        if rownum > 0:
            fVolume.write(row[2] + "\n")
        rownum += 1

fVolume.close()

