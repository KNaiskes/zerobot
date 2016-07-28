################################################################
#Creator : Kiriakos Naiskes
#Contact me at : kiriakosnaiskes@gmail.com
################################################################

import tweepy
import time
from keys import *

#########################
#Add your keys here
#########################

#consumer_key =""
#consumer_secret =""
#access_token =""
#access_token_secret =""


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def tweetIt(message):
	api.update_status(message)
	#Test if tweet is larger thant 140 characters

def retweetIt(username):
	for status in api.user_timeline("@"+username):
		api.retweet(status.id)
		time.sleep(10)
		#Ask for how many tweets they want to retweet

def replyById(tweet_id,username):
	username = "@"+username
	api.update_status(username+" does this work ?",tweet_id )

def replyToWordInMyTimeLine(word):
	myTweets = api.home_timeline()
	for tweet in myTweets:
		if word in tweet.text:
			api.update_status("thanks!")

def sendDirectMessage(username,message):
	if(len(message) <= 140 ):
		api.send_direct_message(screen_name=username,text=message)
	else:
		print "Your message is logner than 140 characters! Aborted"

def listAllFollowes(username):
	for user in tweepy.Cursor(api.followers,screen_name=username).items():
		print user.screen_name
#		print user.id

def printUserTweets(username):
	print "Here are the 20 latest tweets (if there are any or 20)"
	print " "
	for tweets in api.user_timeline(screen_name=username,count=20):
		print tweets.text
	print " "

#tweetIt("testing my function!")
#retweetIt("SophiaHatzi")
#replyById("757467375994302464","SophiaHatzi")
#replyToWordInMyTimeLine("happy")
#sendDirectMessage("SophiaHatzi","this is a message")
#listAllFollowes("SophiaHatzi")
#printUserTweets("SophiaHatzi")
