import tweepy
from textblob import TextBlob


try:
    key = '**********************************'
    secret = '****************************************'

    token = '*************************************************'
    token_secret = '************************************************'   # can't give away access to my twitter on github.

    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token, token_secret)

    api = tweepy.API(auth)

    tweets = api.search('Brexit')

    for twt in tweets:
        print(twt.text)
        analysis = TextBlob(twt.text)
        print(analysis.sentiment)
        print('')
        print('')
        
except:
    
    pass


#api.update_status("...")

#api.update_with_media('...','...')
