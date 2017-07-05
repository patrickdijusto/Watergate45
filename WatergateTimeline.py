#!/usr/bin/python
import twitter
import time
import csv
from settings import *
import datetime

global now
global api

now = datetime.datetime.now()
message = str(now)
print message


print('establish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=OAUTH_TOKEN,
                access_token_secret=OAUTH_SECRET,
                )


print('twitter object established')


##csv_file = csv.reader(open('/storage/Watergate45/wgatetimeline.csv', 'rb'))
csv_file = csv.reader(open('wgatetimeline.csv', 'rb'))
for row in csv_file:
    ##print row
    print str(now.year), row[0]
    if str(now.year) == row[0]:
            print "Same year"
            print str(now.month), row[1]
            if str(now.month) == row[1]:
                print "Same month"
                print str(now.day), row[2]
                if str(now.day) == row[2]:
                    print "Same Day"
                    print row[3]
                    ##print api.PostUpdate(row[3])
                    time.sleep(30)



print "Done"





