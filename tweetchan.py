""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Tweet-Chan                          ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            # A fully automated Twitter-bot #

import time, tweepy

#---------------------Access Keys--------------------------#

consumer_key = 'vU3h2sQQmid7CZ9X32wx2OjMI'
consumer_secret = 'l28UGu7P0Rrswf2mRxLIhrLmfjG595AODalgelYMdB6sfUuc9T'
token_key = '700927951257219072-tZf5z4MFXiBidrobzDFPZSVGdzx2M44'
token_secret = 'RN8rfjCxjMxrHfqs2zGrcM1CbRihzKmqb0KGhuI34hDz6'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token_key,token_secret)
api = tweepy.API(auth)

#----------------------------------------------------------#

file = open('Trumpchan.txt','r')
lines = file.readlines()
file.close()
length=len(lines)

def tweet(lines,length,lineStart):

    if(lineStart>length):
        return

    a = lines[lineStart]

    api.update_status(a)

    time.sleep(60)

    tweet(lines,length,lineStart+20)


tweet(lines,length,0)

print 'complete'




