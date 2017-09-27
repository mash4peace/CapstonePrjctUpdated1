import twitter
import tweepy

#Please feel to use these keys ; I will remove them after presentation
def gettingTweetInfo(info):
    consumer_key = "XJzeM2VqIUaAcy7QZm4zZNeNI"
    consumer_secret = "upTNX9HA1XBWDDTMemFHBgzmHpxz08zGzVzIT94tmLsPIktmZ6"
    access_token = "2925298300-BJWap1LPjwmIstGymM8YmatE2SwvIE2VcWCObR0"
    access_token_secret = "99x1P3GY71iIQQ82Nqs4pyRas8A4937dgfuX1JHmV6ZH6"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    user = api.get_user(info)
    name = user.name
    screenName = user.screen_name
    address = user.location
    followers = user.followers_count
    print(name)
    print(screenName)
    print(address)
    return ("Full name" + name + ", screen name " + screenName + ", location" + address + ", ",  followers, ", of followers " )

""""""
""""
for f in user.friends():
    print(f)

"""
