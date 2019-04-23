# Add your own Quotes
You can add your own quotes to the NocoinShillbot.

**How to add your own quotes:**
1. Fork this repository
2. Open (your) answers.py and add the new quote as the **first** quote in the file.
3. Double check that it looks something like this:
```
answers = random.sample([
"\n\nYour Text Here don't froget "\n\n" at start and no space after the "\n\n". " + Footer ,
"\n\nMy FOMO is at an all time high. " + Footer ,
...], 1)
```
4. Close answers.py
5. Press "create pull request" on your Repository
6. Give it a title
7. Done

# Customizing the bot

1. Add your own keys in keys.py
```
keys = dict(
	consumer_key =          'YourKey',
	consumer_secret =       'YourSecret',
	access_token =          'YourAccessToken',
	access_token_secret =   'YourAccessTokenSecret',
)
```

2. Add/Remove Quotes from answers.py. (\n is Enter on the keyboard, you probably want to remove those)

  2.1 Remove/edit Footer is you want to
```
answers = random.sample([
"This is without Footer. " ,
"This is with Footer. " + Footer], 1)
```

3. Edit sleeptime and sleeptext in twitter_bot.py
```
sleeptime = int(600) //How long does to bot sleep in sec
sleeptext = "10" //How long will the bot sleep in minutes
```

4. Find this line and change EDITME to your keyword(s). To use multiple keyword do "Keyword1 OR Keyword2 OR ..."
```
for s in tweepy.Cursor(api.search, q="EDITME", lang='en').items():
```

5. If you don't have a unique twist to your response based on the keyword in the tweet, delete everything from the first else to the last sleeptime
```
else: 
... 
time.sleep(sleeptime)
```
>Delete

6. Remove List1 to List12
```
List1 = ... 
...        
List12 =... 
```
> Delete

7. Remove message = ... and change Nocoiner to your keyword
```
sn = s.user.screen_name
message = List1 + ans_str //remove
print ("String with \"Nocoiner\" found in tweet " + str(s.id))
```

8. Change "message" in m = ... to "ans_str"
```
m = ".@%s " % (sn) + str(message)
```
to
```
m = ".@%s " % (sn) + str(ans_str)
```

9. Save and run your bot
```
Logging in...
Logged in.
```

10. Lay back and relax

  10b. Get an error
> F



