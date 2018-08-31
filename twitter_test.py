import pytest

from twitter import Twitter

def test_twitter_initialization():
    twitter = Twitter()
    assert twitter

def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet_single("Siemka")
    assert twitter.tweets == ["Siemka"]

def test_tweet_long_messafe():
    twitter=Twitter()
    #Check return exception
    with pytest.raises(Exception):
        twitter.tweet_single('test'*41)
    assert twitter.tweets == []

def test_tweet_with_hashtag():
    twitter= Twitter()
    message= "Twitter #first Message"
    twitter.tweet_single(message)
    assert 'first' in twitter.find_hashtags(message)



