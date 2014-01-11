pp\*.py: Preprocess the sentiment lexicon to generate a positive word file (*_positive.txt) and a negative word file (\*_negative.txt) for the given lexicon.
<br> generateCounts.py: Generates a file for each sentiment lexicon (RawCounts_\*) containing positive/negative/total counts for each day in JSON format
<br> filterCounts.py: Alternative version of generateCounts.py. Perform a key word search on the abstract of each Wall Street Journal article to determine whether it is relevant enough to use as data in the sentiment analysis. Generates a file for each sentiment lexicon (RawCounts_\*) containing positive/negative/total counts for each day in JSON format 
<br> timeseries.py: Generate time series files (timeseries_\*) for all sentiment lexicons and economic indicators. 
<br> simulateTrading.py: Enter 'simulateTrading.py -h' for help
