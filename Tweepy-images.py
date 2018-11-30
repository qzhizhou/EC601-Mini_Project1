import tweepy
from tweepy import OAuthHandler
import json
import wget
import io
import os
import sys

class TweepyAPI():
    def __init__(self,name):
        self.name = name
    def download(self):
        #Twitter API credentials
        consumer_key = 'YOUR-CONSUMER-KEY'
        consumer_secret = 'YOUR-CONSUMER-SECRET'
        access_token = 'YOUR-ACCESS-TOKEN'
        access_secret = 'YOUR-ACCESS-SECRET'

        # def parse(cls, api, raw):
        #     status = cls.first_parse(api, raw)
        #     setattr(status, 'json', json.dumps(raw))
        #     return status

        #authorize twitter, initialize tweepy
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        #grab tweets
        try:
            new_tweets = api.user_timeline(screen_name = self.name,
                                        count=20, include_rts=False,
                                        exclude_replies=True)

            media_files = set()
            for status in new_tweets:
                media = status.entities.get('media', [])
                if(len(media) > 0):
                    media_files.add(media[0]['media_url'])

            for media_file in media_files:
                if media_file.endswith(".jpg"):
                    wget.download(media_file)
                else:
                    print("There is no image in this account")
                    break

        except:
            print("The Twiiter account does not exist!")
        os._exit(0)

