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
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
# import nltk
# nltk.download('vader_lexicon')

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

def percentage(part,whole):
    return 100 * float(part)/float(whole)

def inputkeyword(keyword, noOfTweet) :
       # keyword = input("Please enter keyword or hashtag to search: ")
   # noOfTweet = int(input ("Please enter how many tweets to analyze: "))

   tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)
   positive = 0
   negative = 0
   neutral = 0
   polarity = 0
   tweet_list = []
   neutral_list = []
   negative_list = []
   positive_list = []
   for tweet in tweets:
   
      #print(tweet.text)
      tweet_list.append(tweet.text)
      analysis = TextBlob(tweet.text)
      score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
      neg = score['neg']
      neu = score['neu']
      pos = score['pos']
      comp = score['compound']
      polarity += analysis.sentiment.polarity
      
      if neg > pos:
         negative_list.append(tweet.text)
         negative += 1
      elif pos > neg:
         positive_list.append(tweet.text)
         positive += 1
      elif pos == neg:
         neutral_list.append(tweet.text)
         neutral += 1
   positive = percentage(positive, noOfTweet)
   negative = percentage(negative, noOfTweet)
   neutral = percentage(neutral, noOfTweet)
   polarity = percentage(polarity, noOfTweet)
   positive = format(positive, '.1f')
   negative = format(negative, '.1f')
   neutral = format(neutral, '.1f')
   print(tweet._json)

#Number of Tweets (Total, Positive, Negative, Neutral)
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number:",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))

#Creating PieCart
# labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
# sizes = [positive, neutral, negative]
# colors = ['yellow', 'blue','red']
# patches, texts = plt.pie(sizes,colors=colors, startangle=90)
# plt.style.use('default')
# plt.legend(labels)
# plt.title("Sentiment Analysis Result for keyword= "+keyword+"")
# plt.axis('equal')
# plt.show()

# tweet_list
# tweet_list.drop_duplicates(inplace = True)

#Cleaning Text (RT, Punctuation etc)

#Creating new dataframe and new features
tw_list = pd.DataFrame(tweet_list)
tw_list["text"] = tw_list[0]
# print(tw_list)

#Removing RT, Punctuation etc
remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
rt = lambda x: re.sub("(@[A-Za-z0–9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)
tw_list["text"] = tw_list.text.map(remove_rt).map(rt)
tw_list["text"] = tw_list.text.str.lower()
tw_list.head(10)

#Calculating Negative, Positive, Neutral and Compound values
tw_list[['polarity', 'subjectivity']] = tw_list['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
for index, row in tw_list['text'].items():
   score = SentimentIntensityAnalyzer().polarity_scores(row)
   neg = score['neg']
   neu = score['neu']
   pos = score['pos']
   comp = score['compound']
   if neg > pos:
      tw_list.loc[index, 'sentiment'] = "negative"
   elif pos > neg:
      tw_list.loc[index, 'sentiment'] = "positive"
   else:
      tw_list.loc[index, 'sentiment'] = "neutral"
   tw_list.loc[index, 'neg'] = neg
   tw_list.loc[index, 'neu'] = neu
   tw_list.loc[index, 'pos'] = pos
   tw_list.loc[index, 'compound'] = comp

tw_list.head(10)

#Creating new data frames for all sentiments (positive, negative and neutral)
tw_list_negative = tw_list[tw_list["sentiment"]=="negative"]
tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

def count_values_in_column(data,feature):
   total=data.loc[:,feature].value_counts(dropna=False)
   percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
   return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])
#Count_values for sentiment
count_values_in_column(tw_list,"sentiment")

# create data for Pie Chart
# pichart = count_values_in_column(tw_list,"sentiment")
# names= pichart.index
# size=pichart["Percentage"]
 
# Create a circle for the center of the plot
# my_circle=plt.Circle( (0,0), 0.7, color='white')
# plt.pie(size, labels=names, colors=['green','blue','red'])
# p=plt.gcf()
# p.gca().add_artist(my_circle)
# plt.show()


#Function to Create Wordcloud -all
def create_wordcloud(text):
 mask = np.array(Image.open("WordCloud/mask/bird.png"))
 stopwords = set(STOPWORDS)
 wc = WordCloud(background_color= "white",mask = mask,max_words=3000,stopwords=stopwords,repeat=True)
 wc.generate(str(text))
 wc.to_file("WordCloud/result/wc-all.png")
 print("Word Cloud Saved Successfully")
 path="WordCloud/result/wc-all.png"
 #display(Image.open(path))

#Function Name -Pos
def create_wordcloud_pos(text):
 mask = np.array(Image.open("WordCloud/mask/bird.png"))
 stopwords = set(STOPWORDS)
 wc = WordCloud(background_color= "white",mask = mask,max_words=3000,stopwords=stopwords,repeat=True)
 wc.generate(str(text))
 wc.to_file("WordCloud/result/wc-pos.png")
 print("Word Cloud Saved Successfully")
 path="WordCloud/result/wc-pos.png"

#Function Name -Neg
def create_wordcloud_neg(text):
 mask = np.array(Image.open("WordCloud/mask/bird.png"))
 stopwords = set(STOPWORDS)
 wc = WordCloud(background_color= "white",mask = mask,max_words=3000,stopwords=stopwords,repeat=True)
 wc.generate(str(text))
 wc.to_file("WordCloud/result/wc-neg.png")
 print("Word Cloud Saved Successfully")
 path="WordCloud/result/wc-neg.png"

 #Function Name -Neu
def create_wordcloud_neu(text):
 mask = np.array(Image.open("WordCloud/mask/bird.png"))
 stopwords = set(STOPWORDS)
 wc = WordCloud(background_color= "white",mask = mask,max_words=3000,stopwords=stopwords,repeat=True)
 wc.generate(str(text))
 wc.to_file("WordCloud/result/wc-neu.png")
 print("Word Cloud Saved Successfully")
 path="WordCloud/result/wc-neu.png"

# select sentiment
select = int(input("Please enter 1 Positive | 2 Negative | 3 Neutral | 4 All : "))
 #Creating wordcloud

#Creating wordcloud for positive sentiment
if select == 1:
   create_wordcloud_pos(tw_list_positive["text"].values)

#Creating wordcloud for negative sentiment
elif select == 2:
   create_wordcloud_neg(tw_list_negative["text"].values)

#Creating wordcloud for neutral sentiment
elif select == 3:
   create_wordcloud_neu(tw_list_neutral["text"].values)

#Creating wordcloud for all tweets
elif select == 4:
   create_wordcloud(tw_list["text"].values)

#Calculating tweet’s lenght and word count
tw_list['text_len'] = tw_list['text'].astype(str).apply(len)
tw_list['text_word_count'] = tw_list['text'].apply(lambda x: len(str(x).split()))
round(pd.DataFrame(tw_list.groupby("sentiment").text_len.mean()),2)




