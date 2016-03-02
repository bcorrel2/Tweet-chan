""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                   Tweet-Chan 1.1                       ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#            A fully automated Twitter-bot                 #

import time, tweepy, random

#---------------------Access Keys--------------------------#
"""                  @TweetChan28                        """

consumer_key = 'insert_key_here'
consumer_secret = 'insert_key_here'
token_key = 'insert_key_here'
token_secret = 'insert_key_here'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token_key,token_secret)
api = tweepy.API(auth)

#-----------------------Functions--------------------------#


def checkTweet(lines,length,int): #Function to check text file for invalid tweets
    
    if(int == length):
        return True
    
    post = lines[int]
    
    if(len(post)>140):
        return False
    
    else:
        return checkTweet(lines,length,int+1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def tweetCycle(lastint): #Function to continue tweeting until an invalid tweet is logged
    
    file = open('text.txt','r')
    lines = file.readlines()
    file.close()
    length=len(lines)
    
    valid = checkTweet(lines,length,0)

    if(valid!=True):
        print 'Error: Invalid Tweet(s) Detected'
        return
    
    int = lastint

    while(lastint == int or int == length):
        
        int = random.randrange(0,length)
        
        if (int%2 != 0):
            int+=1

    post = lines[int]
    
    print '-PREPARING-'
    
    try:
        api.update_status(post)
    except:
        tweepy.TweepError

    print time.asctime(time.localtime(time.time()))
    print '-POSTED-'
    print

    
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    
    time.sleep(3600) #30 seconds
    
    tweetCycle(int)

#----------------------------------------------------------#

tweetCycle(-1)

print '==Program Complete=='

#----------------------------------------------------------#




