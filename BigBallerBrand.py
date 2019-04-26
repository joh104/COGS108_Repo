# Import the tweepy library and other libraries
import tweepy
import csv
import os.path
import re
from os import path
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1121130610334912512-JDGgQVfZ0oFYpDEJiqK47sNNggbtVq'
ACCESS_SECRET = 'f35YjmSmptgwX4GcQBthPwhCZQ7T8n1NLhJXzKrdlNDmL'
CONSUMER_KEY = 'mfYU6xUdDVQxKc6Mh3g9Aete4'
CONSUMER_SECRET = 'xkClZZPJYne6QS2JZLkEdZ6YztJjGdjIbZLjeY6pXqpNu66dUe'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
# ---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= True;  will make the api print a notification when Tweepy is waiting for
# rate limits to replenish
# ---------------------------------------------------------------------------------------------------------------------

#initializes list of hashtags to search.
kdHashtags = ["#KevinDurant", "Kevin Durant", "Kevin Durant's", "@KDTrey5",  "Durant", "KD"]
gaHashtags = ["Giannis Antetokounmpo", "Giannis Antetokounmpo's", "@Giannis_An34", "Giannis", "Antetokounmpo's" ]

#list containing tweets about KD
kdTweets = []

#list containing tweets about GA
gaTweets = []

#Number of tweets we want to search for per element inside of the hastag list
numTweets = 20

'''returns sentiment of a given string'''
def SentimentOfTweet(string):
    return TextBlob(string.lower()).sentiment

'''returns sentiment of a given string'''
def BayesSentiment(string):
    return TextBlob(string.lower(), analyzer=NaiveBayesAnalyzer()).sentiment

'''returns list of words from tweets that contain query'''
def searchKDTweets(query, num):
    results = api.search(query, count = num)
    for s in results:
        kdTweets.append( s.text.lower() )
    return kdTweets

'''returns list of words from tweets that contain query'''
def searchGATweets(query, num):
    results = api.search(query, count = num)
    for s in results:
        gaTweets.append( s.text.lower() )
    return gaTweets

# # Query for tweets about KD
# for kdQuery in kdHashtags:
#     searchKDTweets( kdQuery, numTweets)

#Query for tweets about GA
for gaQuery in gaHashtags:
    searchGATweets(gaQuery, numTweets)

# '''Open or create csv file for KD data'''
# with open('KD_Data.csv', 'a') as kd_file:
#     kdwriter = csv.writer(kd_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     '''Create the names of each data column if this file is empty'''
#     if( os.stat('KD_Data.csv').st_size == 0 ):
#         kdwriter.writerow(['Tweet', 'Polarity', 'Subjectivity', 'Positivity', 'Negativity', 'Classification'])
#
#     '''For each tweet that is in kdTweets'''
#     for tweet in kdTweets:
#
#         '''Filter tweet'''
#         tweet = tweet.replace('\n', ' ')
#         tweet = tweet.replace('rt', '')
#         tweet = re.sub(r"http\S+", "", tweet)
#
#         '''Get sentiment data'''
#         sentiment = SentimentOfTweet(tweet)
#         bayes = BayesSentiment(tweet)
#
#         '''Write to csv file'''
#         kdwriter.writerow([tweet.encode('utf-8').strip(), sentiment.polarity, sentiment.subjectivity,
#                            bayes.p_pos, bayes.p_neg, bayes.classification])

'''Open or create csv file for GA data'''
with open('GA_Data.csv', 'a') as ga_file:
    gawriter = csv.writer(ga_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    '''Create the names of each data column if this file is empty'''
    if (os.stat('GA_Data.csv').st_size == 0):
        gawriter.writerow(['Tweet', 'Polarity', 'Subjectivity', 'Positivity', 'Negativity', 'Classification'])

    '''For each tweet that is in gaTweets'''
    for tweet in gaTweets:

        '''Filter tweet'''
        tweet = tweet.replace('\n', ' ')
        tweet = tweet.replace('rt', '')
        tweet = re.sub(r"http\S+", "", tweet)

        '''Get sentiment data'''
        sentiment = SentimentOfTweet(tweet)
        bayes = BayesSentiment(tweet)

        '''Write to csv file'''
        gawriter.writerow([tweet.encode('utf-8').strip(), sentiment.polarity, sentiment.subjectivity,
                           bayes.p_pos, bayes.p_neg, bayes.classification])
