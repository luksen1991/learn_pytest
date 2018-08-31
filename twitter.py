import re


class Twitter(object):
    version=1.0;

    def __init__(self):
        self.tweets=[]

    def tweet_single(self,message):
        if len(message)>150:
            raise Exception("Message to long")
        self.tweets.append(message)

    def find_hashtags(self,message):
        return re.findall("#(\w+) ",message);

