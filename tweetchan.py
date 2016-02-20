""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Tweet-Chan                          ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            # A fully automated Twitter-bot #

import time, tweepy, random

#---------------------Access Keys--------------------------#

consumer_key = 'enter-key-here'
consumer_secret = 'enter-key-here'
token_key = 'enter-key-here'
token_secret = 'enter-key-here'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token_key,token_secret)
api = tweepy.API(auth)

#----------------------------------------------------------#

file = open('tweets.txt','r')
lines = file.readlines()
file.close()
length=len(lines)

#-----------------------Functions--------------------------#

def checkTweet(lines,length,int):
    if(int == length):
        return True

    post = lines[int]
    
    if(len(post)>140):
        return False
    
    checkTweet(lines,length,int+1)

          """"""""""""""""""""""""""""""""""""

def tweetCycle(lines,length,lastint):
    
    int = lastint
    
    while(lastint == int or int == length):

        int = random.randrange(0,length)
    
        if (int%2 != 0):
            int+=1
    
    print int

    post = lines[int]
    
    print post
    
    api.update_status(post)
    
    print '-POSTED-'
    
    time.sleep(60)
    
    tweetCycle(lines,length,int)
    
#----------------------------------------------------------#

valid = checkTweet(lines,length,0)

if(valid==True):
    tweetCycle(lines,length,-1)

else:
    print 'Error: Invalid Tweets Detected'

print '==Program Complete==' #Ideally Should only execute if an invalid list of Tweets is presented.

