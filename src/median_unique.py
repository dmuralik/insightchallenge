#The purpose of this code is to calculate the unique medians per tweet and output the medians
#to a file. Broadly there are 2 sections here: a) reads all the tweets from a file and
#populates a list of medians per tweet b) loops through the list and writes to a file

#Import module for reading command line arguments
import sys

#Initialize filenames to be used in case no arguments are being passed in
inputFileName = 'tweet_input/tweets.txt'
outputFileName = 'tweet_output/ft2.txt'

#Read command line arguments
arguments = sys.argv
#If filenames are not passed in as arguments, fall back on the initialized variables
try:
    inputFileName = arguments[1] if arguments[1] else inputFileName
    outputFileName = arguments[2] if arguments[2] else outputFileName
except IndexError:
    inputFileName = inputFileName

#Read every line from the file and generate a list of count of unique words per line
counts = [len(set(line.split())) for line in open(inputFileName)]

#Going through every item in the above list,generate a list of medians per line
medians = []
for lineIndex, count in enumerate(counts):
    if lineIndex + 1 == 1:
        median = float(counts[lineIndex])
    elif lineIndex % 2 == 0:
        #For a tweet on an odd numbered line, median is exactly half way between first tweet and the current tweet
        median = float(counts[lineIndex / 2])
    else:
        #For a tweet on an even numbered line, median is average of middle 2 tweets
        lowerIndex = lineIndex / 2
        median = (counts[lowerIndex] + counts[lowerIndex + 1]) / float(2)
    medians.insert(lineIndex, median)

#Go through every item in the list of medians and write it to file
outFileHandler = open(outputFileName, 'w')
for lineCounter,median in enumerate(medians):
    outFileHandler.write("%.1f\n" % median)
outFileHandler.close()
