""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Trump-Chan                          ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
      # An comical implemented example of Tweet-Chan #
"""        The Nature of This Program is Satirical.      """
"""    Any Offense Derived From This Program is on You   """
      #              @trump_chan                     #
      
                #MakeAmericaGreatAgain

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

file = open('Trumpchan.txt','r')
lines = file.readlines()
file.close()
length=len(lines)

#-----------------------Functions--------------------------#

def BuildaWall(lines,length,int): #Equivalent to checkTweet()

    if(int == length):
        return True
    
    rhetoric = lines[int] #Equivalent to post
    
    if(len(rhetoric)>140):
        return False

    return BuildaWall(lines,length,int+1)
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def MakeAmericaGreatAgain(lines,length,lastint,x): #Equivalent to tweetCycle()
    
    int = lastint
    
    if (x == 86400): # As currently designed, x will be 86400 24n hours from start.
        x = 0
        print '==MIDNIGHT=='

        try:
            api.update_status("It's a new day. Time to #MakeAmericaGreatAgain!") # Trump starts his Day the American Way
        except:
            tweepy.TweepError

    else:
        while(lastint == int or int == length):
        
            int = random.randrange(0,length)
        
            if (int%2 != 0):
                int+=1

        rhetoric= lines[int]

        print '==PREPARING=='

        try:
            api.update_status(rhetoric)
        except:
            tweepy.TweepError

    print '==POSTED=='
    print time.asctime(time.localtime(time.time()))
    
    for follower in tweepy.Cursor(api.followers).items(): # Amasses an Army of Voters
        follower.follow()
    
    x+=1800
    time.sleep(1800)    # Time shortened to 30 min, because Trump doesn't wait.
    
    MakeAmericaGreatAgain(lines,length,int,x)

#----------------------------------------------------------#

valid = BuildaWall(lines,length,0)

if(valid==True):
    MakeAmericaGreatAgain(lines,length,-1,86400)

else:
    print 'Error: Cruz is using his Dirty Tricks!'

print '==Campaign Complete=='





