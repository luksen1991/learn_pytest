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

@pytest.mark.parametrize("message,hashtag",(
    ("Test #first message",'first'),
    ("#first message",'first'),
    ("#FIRST message",'FIRST')

))
def test_tweet_with_hashtag(message,hashtag):
    twitter=Twitter()
    assert hashtag in twitter.find_hashtags(message)



