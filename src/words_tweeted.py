#The purpose of this code is to generate a list of frequencies of all words in a file containing tweets

#Import module for reading command line arguments
import sys

#Import highperforming container module
from collections import defaultdict

#Initialize filenames to be used in case no arguments are being passed in
inputFileName = 'tweet_input/tweets.txt'
outputFileName = 'tweet_output/ft1.txt'

#Read command line arguments
arguments = sys.argv
#If filenames are not passed in as arguments, fall back on the initialized variables
try:
    inputFileName = arguments[1] if arguments[1] else inputFileName
    outputFileName = arguments[2] if arguments[2] else outputFileName
except IndexError:
    inputFileName = inputFileName

#Initialize a dictionary to store the word counts
wordCount = defaultdict(int)
#Read the file, split the contents into words and loop through each word
for word in open(inputFileName).read().split():
    wordCount[word] += 1


#Go through every item in the generated list and write it to a file
outFileHandler = open(outputFileName, 'w')
for key,value in sorted(wordCount.items()):
    outFileHandler.write("%s,%d\n" %(key, value))
outFileHandler.close()

