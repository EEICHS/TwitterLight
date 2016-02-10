import tweepy
from STRING_MANIPULATION import StringManip
from belleds import Belleds
from time import sleep
##
#b = Belleds()
#b.connect('172.16.0.1')
##
#lights = b.get_lights()


# Consumer keys and access tokens, used for OAuth
consumer_key = 'AuCArJEDT0Bxx2y9ENbhT81Tt'
consumer_secret = 'zuJwQvQeqn0vuNUWjKytDlxcymOWv0Wek6kAOp3ftuUccBmf51'
access_token = '3719272512-51Y4OLMsbmfMn9xoooEoMZ1uGu7akToC3EMEpk3'
access_token_secret = 'jS8ALHHtg4aW4FaVEJ2oxcHDnxD9mcHgcW90upiLfYRxl'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
#api.update_status('Test from EEI coders. We\'re hard at work saving the enviornment right now!')

sM = StringManip()
    
###################################################################

class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
        
        #the_tweeter = status.text
        #sM.colorCheck(the_tweeter)

        sM.colorCheck(status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    while 1 == 1:
        try:
            stream = tweepy.Stream(auth, listener)
            stream.filter(follow=['-2'], track=['#EEI'])
        except:
            pass
