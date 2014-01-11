+ pp\*.py: Preprocess the sentiment lexicon to generate a positive word file (\*\_positive.txt) and a negative word file (\*\_negative.txt) for the given lexicon.
+ generateCounts.py: Generates a file for each sentiment lexicon (RawCounts\_\*) containing positive/negative/total counts for each day in JSON format
+ filterCounts.py: Alternative version of generateCounts.py. Perform a key word search on the abstract of each Wall Street Journal article to determine whether it is relevant enough to use as data in the sentiment analysis. Generates a file for each sentiment lexicon (RawCounts\_\*) containing positive/negative/total counts for each day in JSON format 
+ timeseries.py: Generate time series files (timeseries\_\*) for all sentiment lexicons and economic indicators. 
+ simulateTrading.py: Enter 'simulateTrading.py -h' for help
