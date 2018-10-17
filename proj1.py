# Group 7
# Sara Nabulsi, Sahil Patel, Ujjwal Rehani, William Gao
# CMSC 491 - Social Media Mining
# 10/17/2018

import pymongo 
import sys 
import json 
from collections import Counter 
from prettytable import PrettyTable 
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 

# Try to connect to the MongoDB.
# If it fails then report the error and exit
try: 
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491 
except pymongo.errors.ConnectionFailure as e: 
    print "problem connecting to cmsc491", e
    sys.exit(1)

# Getting the initial Coca Cola data from the Database
print "\n\n******************* COCA COLA *****************\n\n"
hlc = db.CocaCola
tweets = hlc.find({"lang":"en"}) 
texts = []
desc = []

# Printing the amount of tweets we have in our analysis
print "Number of tweets ", tweets.count() 

# Get all the tweet text into a dedicated list
for i in range (26):
    print "TWEET NUMBER", i, "\n"
    print tweets[i]["text"].encode('utf-8')
    print "\n"
    texts.append(tweets[i]["text"])

print "=========================================="

# Splitting up tweets list see how many words are in our vocabulary
words = [] 

for text in texts: 
    # print text.encode('utf-8')
    for w in text.split():
        words.append(w)
# print words 

# Presenting the data to the user
cnt = Counter(words) 
pt = PrettyTable(field_names=['Word', 'Count'])
srtCnt=sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)

for kv in srtCnt:
    pt.add_row(kv)

print pt 

# Performing Lexical Analysis on the Coca Cola tweet texts
print "=========================================="

print "Lexical Diversity for Coca Cola"

print 1.0*len(set(words))/len(words)


print "Sentiment Analysis for Pepsi"
for i in range (26):
    if (tweets[i]["user"]["description"] is not None):
        vs = vaderSentiment(tweets[i]["text"].encode('utf-8'))
        print"\n\t"+str(vs['compound'])
        print tweets[i]["text"].encode('utf-8') 
        print "========================================\n"
        desc.append(tweets[i]["text"])




#################################################################################

# Getting the initial Pepsi data from the Database
print "\n\n******************* PEPSI *****************\n\n"

hlc = db.pepsi
tweets = hlc.find({"lang":"en"}) 
texts = []

# Printing the amount of tweets we have in our analysis
print "Number of tweets ", tweets.count() 

# Get all the tweet text into a dedicated list
for i in range (26):
    print "TWEET NUMBER", i, "\n"
    print tweets[i]["text"].encode('utf-8')
    print "\n"
    texts.append(tweets[i]["text"])
print "=========================================="

# Splitting up tweets list see how many words are in our vocabulary
words = [] 

for text in texts: 
    # print text.encode('utf-8')
    for w in text.split():
        words.append(w)
# print words 

# Presenting the data to the user
cnt = Counter(words) 
pt = PrettyTable(field_names=['Word', 'Count'])
srtCnt=sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)

for kv in srtCnt:
    pt.add_row(kv)

print pt 

# Performing Lexical Analysis on the Pepsi tweet texts
print "=========================================="

print "Lexical Diversity for Pepsi"

print 1.0*len(set(words))/len(words)

print "Sentiment Analysis for Pepsi"

for i in range (26):
    if (tweets[i]["user"]["description"] is not None):
        vs = vaderSentiment(tweets[i]["text"].encode('utf-8'))
        print"\n\t"+str(vs['compound'])
        print tweets[i]["text"].encode('utf-8') 
        print "========================================\n"
        desc.append(tweets[i]["text"])
