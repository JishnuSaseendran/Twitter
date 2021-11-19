import json
import oauth2 as oauth

name = raw_input('Twitter Name = ')

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_token_secret)
client = oauth.Client(consumer, access_token)


url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=20"

response, data = client.request( url )

tweets = json.loads(data)
for tweet in tweets:
    print (tweet['text'])
    #print (data)
