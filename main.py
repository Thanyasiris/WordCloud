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

# 1000 is width of window and 600 is the height
#,mode='firefox-app'
eel.start('index.html',mode='firefox-app',port=8080, size=(1000, 600))
