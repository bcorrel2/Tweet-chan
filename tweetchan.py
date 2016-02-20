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

def tweet(lines,length):
    
    int = random.randrange(0,length)
    
    if (int%2 != 0):
        int+=1
    if (int == length):
        int-=3
    
    print int

    post = lines[int]

    print post

    api.update_status(post)

    print '-POSTED-'
    
    time.sleep(360)

    tweet(lines,length)


tweet(lines,length) #Instigates Infinite Loop. Each cycle will post a Tweet, then sleep for a specified amount of time.

print '-COMPLETE-' #Ideally, this should never be printed. The ideal scenario is an infinite loop.




