""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Tweet-Chan 1.0                      ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#              A fully Automated Twitter-bot               #

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

file = open('text.txt','r')
lines = file.readlines()
file.close()
length=len(lines)

#-----------------------Functions--------------------------#

def checkTweet(lines,length,int): #Function checks that every tweet is a valid tweet

    if(int == length):
        return True
    
    post = lines[int]
    
    if(len(post)>140):
        return False

    else:
        return checkTweet(lines,length,int+1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def tweetCycle(lines,length,lastint): #Function recurses indefinelty, sleeping between recurses.
    
    int = lastint
    
    while(lastint == int or int == length):

        int = random.randrange(0,length)
    
        if (int%2 != 0): # All quotes are held on even lines
            int+=1

    post = lines[int]
    
    print '-PREPARING-'
    
    try:
        api.update_status(post)
    except:
        tweepy.TweepError
    
    print '-POSTED-'
    print time.asctime(time.localtime(time.time()))

    for follower in tweepy.Cursor(api.followers).items(): # Automatically Follows Any User that Follows the Bot
        follower.follow()
    
    time.sleep(3600) # 1 hr intervals between tweets
    
    tweetCycle(lines,length,int)

#----------------------------------------------------------#

valid = checkTweet(lines,length,0) 

if(valid==True):
    tweetCycle(lines,length,-1)

else:
    print 'Error: Invalid Tweets Detected'

print '==Program Complete=='
