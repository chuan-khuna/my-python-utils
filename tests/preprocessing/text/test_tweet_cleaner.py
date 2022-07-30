from utils.preprocessing.text.tweet_cleaner import TweetCleaner
from utils.preprocessing.text.text_cleaner import TextCleaner
import pytest

def test_tweet_cleaner_is_inherited_from_text_cleaner():
    cleaner = TweetCleaner()
    assert isinstance(cleaner, TweetCleaner)
    assert isinstance(cleaner, TextCleaner)

# how to test 4 principles of OOP and SOLID

# tweet cleaner extra features
# tweet cleaner should be able to get user_id, rt_id
# tweet cleaner should be able to get emoji