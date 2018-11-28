# Twitter-text-analysis
Basic tweet download and analysis.

Quick start
1. Apply for access https://developer.twitter.com/
2. Write codes in final_stream_listener.py 
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
3. Set filter
myStream.filter(track=['track'])

In class MyStreamListener is writer, we can write there what part of tweet we want to save. At https://developer.twitter.com/ we can see anatomy of tweet. If you change this remember to edit first writerow in text_analysis.py
