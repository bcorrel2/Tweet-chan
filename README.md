# Tweet-chan
Automated Twitter-Bot v1.1.0 3/1/16

Current active accounts include:
    @trump_chan
    
Current inactive accounts include:
    @TweetChan28

***Update Notes***

-Program now reads text.txt every hour. This will allow new tweets added to the file to quickly and eaily be added into the bots database. In previous versions, the bot had to be stopped before the tweets could be changed.

***Conception***

Tweet-chan was concieved and programmed at the 2016 HackIllinois Hackathon. The goal of Tweet-chan was to develop a powerful script with real world implictions using simple python code. After reading an article about Twitter-bots, I stumbled upon Tweepy, an API that intrigued me. Thus, I decided to use it to create my own personal Twitter-bot.

***Tweet-chan***

Tweet-chan works in 2 steps:

Step 1: Upon activation, Tweet-chan will take a simple text file and scan it for invalid tweets. If an invalid tweet is found, the user is notified and the program finishes. 

Step 2: Tweet-chan will activate a cycle that will loop indefintely. The cycle begins with with Tweet-chan choosing a random tweet and posting it. Tweet-chan will then look for new followers. Tweet-chan will follow any user who follows it. The cycle ends with Tweet-chan putting itself to sleep. After this period is over, the function recurses and the cycle begins anew. 

The bot itself runs on a Raspberry Pi. This allows it to run 24/7.

An implementation of Tweet-chan, Trump-chan, is currently running. The purpose of the bot is to produce Donald Trump quotes every half-hour.

***About text.txt***

Thanks to built-in tweet-detection, Tweet-chan is able to take many types of text file. To create a text file for Tweet-chan, input a tweet that does not exceede 140 characters. Each tweet added should be seperated by a blank line. Reference trumpchan.txt to see how the text file should be formatted. 
    
***About Trump-chan***

Trump-chan is a comical implementation of tweetchan.py. Utilizing firey quotes and patriotic variables, Trump-chan is top-of-the-line in automated presidental candidates. 

All quotes used by Trump-chan are real or variations of real quotes. Tweets made by Trump-chan do not neccessarily reflect those of Tweet-chan or it's developer. 

***Future of Tweet-chan***

The future of Tweet-chan is unclear. At a later date, it is my intention to add an app interface to the program. Whether the app will expand into a larger creation or remain a small pet-project remains to be seen. For now, please enjoy Tweet-chan and, by extension, Trump-chan.
