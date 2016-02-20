""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Tweet-Chan                          ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            # A fully automated Twitter-bot #

import time, tweepy

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

def tweet(lines,length,lineStart):

    if(lineStart>length):
        return

    a = lines[lineStart]

    api.update_status(a)

    time.sleep(360)

    tweet(lines,length,lineStart+2)


tweet(lines,length,0)

print 'complete'




