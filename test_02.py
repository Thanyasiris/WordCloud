#Sentiment Analysis
# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
import collections
import json
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from dotenv import load_dotenv
from pymongo import MongoClient
import en_core_web_sm

#https://medium.com/analytics-vidhya/visualizing-your-data-from-mongodb-to-word-cloud-with-python-3-3e9c4b4f2743

#establing connection
try:
    connect = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# connecting or switching to the database
db = connect.wordCloud

# creating or switching to demoCollection
collection = db.wordCloudCollection

# import access Twitter API from .env
load_dotenv()

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth)

def find_document(collection, query):
    documents = []
    cursor = db[collection].find(query)
    for document in cursor:
        documents.append(document)
    return documents

def load_data(collection, data_entry):
    docs = MongoRepository.find_document(collection, {})
    details = []
    for doc in docs:
        details.append(doc[data_entry])
    return details

nlp = en_core_web_sm.load()

symbols_to_replace = {'&': ' ', '#': ' ', '$': ' ', '£': ' ', '(': ' ', ')': ' ', '%': ' ', ':': ' ', '+': ' ',
                      '-': ' ', '*': ' ', '/': ' ', '<': ' ', '=': ' ', '>': ' ', '?': ' ', '@': ' ', '[': ' ',
                      ']': ' ', "\\": ' ', '^': ' ', '_': ' ', '`': ' ', '{': ' ', '}': ' ', '|': ' ', '~': ' ',
                      '”': ' ', '\t': ' ', '\n': ' ', '\r': ' ', '\v': ' ', '\f': ' '}

symbols_translator = str.maketrans(symbols_to_replace)
content = content.translate(symbols_translator)
doc = nlp(content)

# Retrieve all ORGs and PERSONs
org_and_persons = []
for ent in doc.ents:
    if ent.label_ == 'PERSON' or ent.label_ == 'ORG':
        org_and_persons.append(ent.text)

# Tokenize ORGs and PERSONs for filtering
all_org_persons = ''
for org_and_person in org_and_persons:
    all_org_persons += org_and_person + ' '
org_persons_doc = nlp(all_org_persons)
org_persons_tokens = []
for token in org_persons_doc:
    org_persons_tokens.append(token.text)

result = []
for token in doc:
    if not token.is_punct and not token.is_stop:
        if token.text not in org_persons_tokens:
            if (len(token.text) == 1 and token.pos_ == 'NUM') or len(token.text) > 1:
                result.append(token.lemma_.lower().strip())

# Exclude stop words
stop_words = load_stop_words()
result = [k.lower().strip() for k in result if k not in stop_words and k is not '']


def load_stop_words():
    stop_words_file = path.join(base_dir, "analyzer/resources/stop-words.txt")
    with open(stop_words_file) as f:
        stop_words_content = f.readlines()
    stop_words = [x.strip() for x in stop_words_content]
    logging.info(f'Loaded stop words: {stop_words}')
    return stop_words