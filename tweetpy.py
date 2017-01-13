import json
import oauth2 as oauth

name = raw_input('Twitter Name = ')

consumer_key = "9FN6sRd96iKAxX3lJJEIPc8HO"
consumer_secret = "rv8q3fPwGb5tbJLhLrxYj8O1ErXDAYNPbwr3YuckQDYTilvwqY"

access_token = "130107221-VhCIcNqXER4SQP9FFqOiwv0Z9Zaz5HRtheGqRFWj"
access_token_secret = "ruKsDTrJN70Ays6A0psUxd7h9bHnNwVVA0s8G8dW82XWk"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_token_secret)
client = oauth.Client(consumer, access_token)


url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=20"

response, data = client.request( url )

tweets = json.loads(data)
for tweet in tweets:
    print (tweet['text'])
    #print (data)
