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

global RTOfMe
global rex
global wong
global wing
global wers


def retweets():
        global RetweetUsers
        RetweetUsers=[]
        print "Printing retweets"
        print

        RTOfMe = api.GetRetweetsOfMe()
        print([u.id for u in RTOfMe])
        print
        for u in RTOfMe:
                global rex
                time.sleep(5)
                rex = api.GetRetweeters(u.id)
                print 'printing rex...'
                print rex
                print "Printing retweet users..."
                RetweetUsers.extend(rex)
                print RetweetUsers

			

			


def mentions():
        print "Printing mentions"
        print
        wong = api.GetMentions()
        print([u.screen_name for u in wong])
        print
        print wong
        print



def followers():
        print "Printing followers"
        print
        global wers
        wers = api.GetFollowers()
        print([u.screen_name for u in wers])
        print
        print wers
        print

def friends():
        print "Printing friends"
        print
        global wing
        wing = api.GetFriends()
        print([u.screen_name for u in wing])
        print
        print wing
        print


def cleanupRetweets():
        print
        print "printing RetweetUsers"
        print RetweetUsers
        print
        a = 0
        lex = len(RetweetUsers)
        while a < lex:
                print "A, value of A"
                valA = RetweetUsers[a]
                print a, valA
                l = RetweetUsers.count(valA)
                print "Number of occurrences: "                
                print l
                for b in range(1,l):
                        RetweetUsers.remove(valA)
                        print RetweetUsers
                a = a+1
                lex = len(RetweetUsers)
                print RetweetUsers
        



retweets()
cleanupRetweets()


followers()
friends()




for u in wing:
        if wers.count(u):
                wers.remove(u)

print "printing for u in wing, remove rex"
for u in wing:	
        print u.id
        print u.screen_name
        RetweetUsers.remove(u.id)


print RetweetUsers
print wers

print([u.screen_name for u in wers])

for u in wers:
        #api.CreateFriendship(u.id)
        print "Just pretended to became friends with", u.screen_name
        time.sleep(5)

for r in RetweetUsers:
        #api.CreateFriendship(r)
        print "Just pretended to became friends with", r
        time.sleep(5)
        

	
friends()
	
