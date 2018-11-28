import tweepy
from tweepy import OAuthHandler
import csv

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open('data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)		
            writer.writerow([status.created_at, status.text, status.author.screen_name])
            print(status.text)
	
        
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(["created_at", "text", "screen_name"])
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['track'])
