"""
Author:Shivam Singh
Email:mavish043@gmail.com
Contact:9718496646
"""
import os
import json
import twitter
from elasticsearch import Elasticsearch

#
# Create Twitter Stream by Twitter OAuth in OS environment.
#
"""def init():
    es_index()
    start_server() """
def connect_twitter_stream():
    """
    You need to set os environment like 'export TWITTER_CONSUMER_KEY=YOUR KEY'.
    """
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    auth = twitter.OAuth(token=access_token,token_secret=access_token_secret,consumer_key=consumer_key,consumer_secret=consumer_secret)
    return twitter.TwitterStream(auth=auth)



def put_stream(es, twitter_stream,tweet_data):

    tweets = twitter_stream.statuses.sample()
    for twe in tweet_data:
        tweets = twitter_stream.statuses.filter(track=twe)
        for tweet in tweets:
        #print(json.dumps(tweet,indent=4,sort_keys=True))
            dic = {
                    'tweet_id': tweet['id'],
                    'screen_name': tweet['user']['screen_name'],
                    'text': tweet['text'],
                    'retweet_count':tweet['retweet_count'],
                    #'favourite_count':tweet['favourite_count'],
                    #'followers_count':tweet['followers_count'],
                    'lang':tweet['lang'],
                    'tweet_date':tweet['created_at'],
                }
            if 'followers_count'in tweet:
                dic['followers_count'] = tweet['followers_count']

            if  'favourite_count' in tweet:
                dic['favourite_count']=tweet['favourite_count']
            if 'urls' in tweet:
                dic['urls']=tweet['urls']['url']
            if  'user_mentions' in tweet:
                dic['user_mentions']=tweet['user_mentions']['screen_name']
            if tweet['entities']['hashtags']:
                    # hash tags is array.
                dic['hashtags'] = tweet['entities']['hashtags']

                es.index(index="twitter", doc_type='tweet', body=dic)
                # dict to JSON.
            print(json.dumps(dic, ensure_ascii=False))
def es_index():
    es = Elasticsearch()
    twitter_stream = connect_twitter_stream()
    tweet_data=['holi','hack','modi','sridevi']
    put_stream(es, twitter_stream,tweet_data)


