# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1220392858336677888-9XQlXaTPp6JZQU1diIOu3iG5emKUy8'
ACCESS_SECRET = 'GQzCsbr8XPDLKwWkPVx9YYaM6euUUFdnv9RX8PXyXZUC1'
CONSUMER_KEY = 'LTR1KSkdZH8zEHRWxbT2enRki'
CONSUMER_SECRET = 'qDkfJOBC1mfqW3i8CcLy6a8dLenarNO1iRC5cVIaKPy1kDjsd0'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

for status in tweepy.Cursor(api.search_tweets, q='#เอเปค').items(1):
    print(status._json)

#print(json.dumps(status._json, indent=4))
#for status in tweepy.Cursor(api.home_timeline).items(5):
#	print(status._json)
	
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------