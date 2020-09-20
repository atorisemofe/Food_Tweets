import os
import tweepy as tw
import pandas as pd
import requests
import flask
from flask import Flask
import random

app = Flask(__name__, template_folder="templates1")

consumer_key1= os.environ['consumer_key']
consumer_secret1= os.environ['consumer_secret']
access_token1= os.environ['access_token']
access_token_secret1= os.environ['access_token_secret']

auth = tw.OAuthHandler(consumer_key1, consumer_secret1)
auth.set_access_token(access_token1, access_token_secret1)
api = tw.API(auth, wait_on_rate_limit=True)

@app.route('/')
def index():
    Food_tags = ["#foodie", "#foodlover", "#homemade", "#foodblogger", "#instafood",
                 "#foodphotography", "#foodstagram", "#yummy", "#delicious", "#healthy", 
                 "#eat", "#tasty", "#dessert", "#breakfast", "pizza", "chicken", "tacos", "ice cream"]
    search_words = random.choice(Food_tags)
    print(search_words)
    print("reached index method")
    date_since = "2019-09-16"
    tweet_list = []
    tweet_time = []
    tweet_author = []
    
    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(5)
    tweets
    
    for tweet in tweets:
        tweet_list.append(tweet.text)
        tweet_time.append(tweet.created_at)
        tweet_author.append(tweet.user.screen_name)
        
    return flask.render_template(
        "index.html",
        tweet_list = tweet_list,
        tweet_time = tweet_time,
        tweet_author = tweet_author,
        hashtag = search_words,
        list_len = len(tweet_list),
        time_len = len(tweet_time),
        ) 
        
        
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
    )
