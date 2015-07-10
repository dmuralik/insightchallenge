#!/usr/bin/env bash
#If run on any version of linux or Mac OSX, python should be most likely available
#In case of Windows, Python needs to be downloaded from https://www.python.org/downloads/, installed and Python's installed dir added to PATH variable

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

