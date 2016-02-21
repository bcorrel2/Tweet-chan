""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##                    Trump-Chan                          ##
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
      # An comical implemented example of Tweet-Chan #
"""        The Nature of This Program is Satirical.      """
"""    Any Offense Derived From This Program is on You   """

                #MakeAmericaGreatAgain

import time, tweepy, random

#---------------------Access Keys--------------------------#

consumer_key = 'zg6oEHsCSWFrkOKyxaauAFYf4'
consumer_secret = 'RrVxM5yGKXd2HVdLnKG3ALismW8ccCHJijKrdbD5tuvJu7Oqk4'
token_key = '701080374022172672-3ievNFd2UhFdHy6rETIePMa4mgmcd1Q'
token_secret = '2hz3ap9hO7T0PO8iEsqmLrBTHzpsmY9LyqKlbK7TINhbZ'

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




