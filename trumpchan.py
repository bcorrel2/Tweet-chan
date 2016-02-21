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
    
    rhetoric = lines[int]
    
    if(len(rhetoric)>140):
        return False

    return BuildaWall(lines,length,int+1)
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def MakeAmericaGreatAgain(lines,length,lastint): #Equivalent to tweetCycle()
    
    int = lastint
    
    while(lastint == int or int == length):
        
        int = random.randrange(0,length)
        
        if (int%2 != 0):
            int+=1

    rhetoric= lines[int]

    print '==NEW TWEET=='
    print rhetoric
    
    api.update_status(rhetoric)
    
    print '=POSTED='
    
    time.sleep(60)
    
    MakeAmericaGreatAgain(lines,length,int)

#----------------------------------------------------------#

valid = BuildaWall(lines,length,0)

if(valid==True):
    MakeAmericaGreatAgain(lines,length,-1)

else:
    print 'Error: Jeb Bush is a waste of space'

print '==Campaign Complete=='




