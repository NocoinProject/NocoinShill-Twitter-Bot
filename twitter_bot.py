import tweepy
import time
import os
from keys import keys
from answers import answers

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

sleeptime = int(600)
sleeptext = "10"

List1 = "> 'Nocoiner'"
List2 = "> 'nocoiner'"
List3 = "> 'No coiner'"
List4 = "> 'no coiner'"
List5 = "> 'Nocoin'"
List6 = "> 'NoCoin'"
List7 = "> 'Nocoiners'"
List8 = "> 'nocoiners'"
List9 = "> 'No-coiner'"
List10 = "> 'no-coiner'"
List11 = "> 'No-coiners'"
List12 = "> 'no-coiners'"
                        
ans_str = ''.join(answers)

def follow(api):
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Followed everyone that is following " + str(follower.id))
        print ("Sleeping for 60 seconds...")
        time.sleep(60)

def bot_login():
        print ("Logging in...")
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        print ("Logged in!")
        
        return api

def me(api):
        bot = api.me()
        print (bot.name)

        return bot


def run_bot(api, bot, tweets_replied_to):
    print ("Searching last 100 Tweets...")

    for s in tweepy.Cursor(api.search, q="Nocoiner OR nocoiner OR No coiner OR no coiner OR Nocoin OR NoCoin OR Nocoiners OR nocoiners OR No-coiner OR no-coiner OR No-coiners OR no-coiners", lang='en').items():
        print("Bleep Bloop.")
        if "Nocoiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
           sn = s.user.screen_name
           message = List1 + ans_str
           print ("String with \"Nocoiner\" found in tweet " + str(s.id))
           m = ".@%s " % (sn) + str(message)
           print ("Replied to tweet " + str(s.id))
           s = api.update_status(m, s.id)

           tweets_replied_to = []; 
           tweets_replied_to.append(s.id)

           with open ("tweets_replied_to.txt", "a") as f:
                       f.write(str(s.id) + "\n")
            
           print ("Sleeping for " + sleeptext + " minutes...")

           time.sleep(sleeptime)

        else:
            if "nocoiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
               sn = s.user.screen_name
               message = List2 + ans_str
               print ("String with \"nocoiner\" found in tweet " + str(s.id))
               m = ".@%s " % (sn) + str(message)
               print ("Replied to tweet " + str(s.id))
               s = api.update_status(m, s.id)

               tweets_replied_to = []; 
               tweets_replied_to.append(s.id)

               with open ("tweets_replied_to.txt", "a") as f:
                           f.write(str(s.id) + "\n")
            
               print ("Sleeping for " + sleeptext + " minutes...")
                                        
               time.sleep(sleeptime)

            else:
                if "No coiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                   sn = s.user.screen_name
                   message = List3 + ans_str
                   print ("String with \"No coiner\" found in tweet " + str(s.id))
                   m = ".@%s " % (sn) + str(message)
                   print ("Replied to tweet " + str(s.id))
                   s = api.update_status(m, s.id)

                   tweets_replied_to = []; 
                   tweets_replied_to.append(s.id)

                   with open ("tweets_replied_to.txt", "a") as f:
                               f.write(str(s.id) + "\n")
                               
                   print ("Sleeping for " + sleeptext + " minutes...")
                                        
                   time.sleep(sleeptime)

                else:
                     if "no coiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                        sn = s.user.screen_name
                        message = List4 + ans_str
                        print ("String with \"no coiner\" found in tweet " + str(s.id))
                        m = ".@%s " % (sn) + str(message)
                        print ("Replied to tweet " + str(s.id))
                        s = api.update_status(m, s.id)

                        tweets_replied_to = []; 
                        tweets_replied_to.append(s.id)

                        with open ("tweets_replied_to.txt", "a") as f:
                                    f.write(str(s.id) + "\n")
                       
                        print ("Sleeping for " + sleeptext + " minutes...")
                                        
                        time.sleep(sleeptime)

                     else:
                         if "Nocoin " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                            sn = s.user.screen_name
                            message = List5 + ans_str
                            print ("String with \"Nocoin\" found in tweet " + str(s.id))
                            m = ".@%s " % (sn) + str(message)
                            print ("Replied to tweet " + str(s.id))
                            s = api.update_status(m, s.id)

                            tweets_replied_to = []; 
                            tweets_replied_to.append(s.id)

                            with open ("tweets_replied_to.txt", "a") as f:
                                        f.write(str(s.id) + "\n")
                
                            print ("Sleeping for " + sleeptext + " minutes...")
                                        
                            time.sleep(sleeptime)

                         else:
                             if "NoCoin " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                sn = s.user.screen_name
                                message = List6 + ans_str
                                print ("String with \"NoCoin\" found in tweet " + s.id)
                                m = ".@%s " % (sn) + str(message)
                                print ("Replied to tweet " + str(s.id))
                                s = api.update_status(m, s.id)
                                
                                tweets_replied_to = []; 
                                tweets_replied_to.append(s.id)

                                with open ("tweets_replied_to.txt", "a") as f:
                                            f.write(str(s.id) + "\n")
              
                                print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                time.sleep(sleeptime)

                             else:
                                 if "Nocoiners" in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                    sn = s.user.screen_name
                                    message = List7 + ans_str
                                    print ("String with \"Nocoiners\" found in tweet " + str(s.id))
                                    m = ".@%s " % (sn) + str(message)
                                    print ("Replied to tweet " + str(s.id))
                                    s = api.update_status(m, s.id)
                                    
                                    tweets_replied_to = []; 
                                    tweets_replied_to.append(s.id)

                                    with open ("tweets_replied_to.txt", "a") as f:
                                                f.write(str(s.id) + "\n")
                                            
                                    print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                    time.sleep(sleeptime)

                                 else:
                                     if "nocoiners" in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                        sn = s.user.screen_name
                                        message = List8 + ans_str
                                        print ("String with \"nocoiners\" found in tweet " + str(s.id))
                                        m = ".@%s " % (sn) + str(message)
                                        print ("Replied to tweet " + str(s.id))
                                        s = api.update_status(m, s.id)
                                        
                                        tweets_replied_to = []; 
                                        tweets_replied_to.append(s.id)

                                        with open ("tweets_replied_to.txt", "a") as f:
                                                    f.write(str(s.id) + "\n")
                                                    
                                        print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                        time.sleep(sleeptime)

                                     else:
                                         if "No-coiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                            sn = s.user.screen_name
                                            message = List9 + ans_str
                                            print ("String with \"No-coiner\" found in tweet " + str(s.id))
                                            m = ".@%s " % (sn) + str(message)
                                            print ("Replied to tweet " + str(s.id))
                                            s = api.update_status(m, s.id)
                                            
                                            tweets_replied_to = []; 
                                            tweets_replied_to.append(s.id)

                                            with open ("tweets_replied_to.txt", "a") as f:
                                                        f.write(str(s.id) + "\n")
                                            
                                            print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                            time.sleep(sleeptime)

                                         else:
                                             if "no-coiner " in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                                sn = s.user.screen_name
                                                message = List10 + ans_str
                                                print ("String with \"no-coiner\" found in tweet " + str(s.id))
                                                m = ".@%s " % (sn) + str(message)
                                                print ("Replied to tweet " + str(s.id))
                                                s = api.update_status(m, s.id)
                                                
                                                tweets_replied_to = []; 
                                                tweets_replied_to.append(s.id)

                                                with open ("tweets_replied_to.txt", "a") as f:
                                                            f.write(str(s.id) + "\n")
                                            
                                                print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                                time.sleep(sleeptime)

                                             else:
                                                 if "No-coiners" in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                                    sn = s.user.screen_name
                                                    message = List11 + ans_str
                                                    print ("String with \"No-coiners\" found in tweet " + str(s.id))
                                                    m = ".@%s " % (sn) + str(message)
                                                    print ("Replied to tweet " + str(s.id))
                                                    s = api.update_status(m, s.id)
                                                    
                                                    tweets_replied_to = []; 
                                                    tweets_replied_to.append(s.id)

                                                    with open ("tweets_replied_to.txt", "a") as f:
                                                                f.write(str(s.id) + "\n")
                                            
                                                    print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                                    time.sleep(sleeptime)

                                                 else:
                                                     if "no-coiners" in s.text and s.user.name != bot.name and s.id not in tweets_replied_to:
                                                        sn = s.user.screen_name
                                                        message = List12 + ans_str
                                                        print ("String with \"no-coiners\" found in tweet " + str(s.id))
                                                        m = ".@%s " % (sn) + str(message)
                                                        print ("Replied to tweet " + str(s.id))
                                                        s = api.update_status(m, s.id)
                                                        
                                                        tweets_replied_to = []; 
                                                        tweets_replied_to.append(s.id)

                                                        with open ("tweets_replied_to.txt", "a") as f:
                                                                    f.write(str(s.id) + "\n")
                                            
                                                        print ("Sleeping for " + sleeptext + " minutes...")
                                        
                                                        time.sleep(sleeptime)



def get_saved_tweets():
        if not os.path.isfile("tweets_replied_to.txt"):
                tweets_replied_to = []
        else:
                with open("tweets_replied_to.txt", "r") as f: 
                        tweets_replied_to = f.read()
                        tweets_replied_to = tweets_replied_to.split("\n") 

        return tweets_replied_to

    
api = bot_login()
bot = me(api)
tweets_replied_to = get_saved_tweets()
print (tweets_replied_to)

while True:
        print ("Sleeping for 15 seconds...")
        time.sleep(15)
        run_bot(api, bot, tweets_replied_to)


# END #
