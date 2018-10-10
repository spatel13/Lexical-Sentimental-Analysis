import pymongo 
import sys 
import json 
from collections import Counter 
from prettytable import PrettyTable 
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 


try: 
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491 
except pymongo.errors.ConnectionFailure as e: 
    print "problem connecting to cmsc491", e
    sys.exit(1)


print "\n\n******************* COCA COLA *****************\n\n"
hlc = db.CocaCola
tweets = hlc.find({"lang":"en"}) 
texts = []
desc = []


print "Number of tweets ", tweets.count() 


for i in range (26):
    print "TWEET NUMBER", i, "\n"
    print tweets[i]["text"].encode('utf-8')
    print "\n"
    texts.append(tweets[i]["text"])

print "=========================================="

words = [] 

for text in texts: 
    #print text.encode('utf-8')
    for w in text.split():
        words.append(w)
#print words 


cnt = Counter(words) 
pt = PrettyTable(field_names=['Word', 'Count'])
srtCnt=sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)

for kv in srtCnt:
    pt.add_row(kv)

print pt 

print "=========================================="

print "Lexical Diversity for Coca Cola"

print 1.0*len(set(words))/len(words)


print "Sentiment Analysis for Pepsi"
for i in range (26):
    if (tweets[i]["user"]["description"] is not None):
        vs = vaderSentiment(tweets[i]["user"]["description"].encode('utf-8'))
        print"\n\t"+str(vs['compound'])
        print tweets[i]["user"]["description"].encode('utf-8') 
        print "========================================\n"
        desc.append(tweets[i]["user"]["description"])




#################################################################################

print "\n\n******************* PEPSI *****************\n\n"

hlc = db.pepsi
tweets = hlc.find({"lang":"en"}) 
texts = []


print "Number of tweets ", tweets.count() 


for i in range (26):
    print "TWEET NUMBER", i, "\n"
    print tweets[i]["text"].encode('utf-8')
    print "\n"
    texts.append(tweets[i]["text"])
print "=========================================="

words = [] 

for text in texts: 
    #print text.encode('utf-8')
    for w in text.split():
        words.append(w)
#print words 


cnt = Counter(words) 
pt = PrettyTable(field_names=['Word', 'Count'])
srtCnt=sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)

for kv in srtCnt:
    pt.add_row(kv)

print pt 

print "=========================================="

print "Lexical Diversity for Pepsi"

print 1.0*len(set(words))/len(words)

print "Sentiment Analysis for Pepsi"

for i in range (26):
    if (tweets[i]["user"]["description"] is not None):
        vs = vaderSentiment(tweets[i]["user"]["description"].encode('utf-8'))
        print"\n\t"+str(vs['compound'])
        print tweets[i]["user"]["description"].encode('utf-8') 
        print "========================================\n"
        desc.append(tweets[i]["user"]["description"])
