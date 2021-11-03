import tweepy
import time 
import OAUTH

#Login info
consumer_key = OAUTH.api_key
consumer_secret = OAUTH.api_secret
access_token = OAUTH.bearer_token
access_token_secret = OAUTH.token_secret

#Connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print("I'm replying...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")
    for mention in reversed(mentions):
        print(str(mention.id) + " - " + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#woogang" in mention.full_text.lower():
            print("woogang enabled")
            print("responding...")
            api.update_status("@" + mention.user.screen_name + " WOOOOOOOOO", mention.id)
        elif mention.user.screen_name == "Noname1":
            api.update_status("@" + mention.user.screen_name + " je t'aime <3", mention.id)
        elif mention.user.screen_name == "Noname2":
            api.update_status("@" + mention.user.screen_name + " spa drôle", mention.id)
        else:
            api.update_status("@" + mention.user.screen_name + " thks dude", mention.id)


while True:
    reply_to_tweets()
    time.sleep(20)