################################################################
#Creator : Kiriakos Naiskes
#Contact me at : kiriakosnaiskes@gmail.com
################################################################

import tweepy
import time
from keys import * # I keep my keys in an another file so they won't be exposed to the public

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

def addDelay():
	time.sleep(15) #Add a delay of 15 seconds, so bot won't get banned

def checkChars(chars):
	if(len(chars) <= 140):
		return True
	while(len(chars) > 140):
		print "Text must be less than 140 characters, try again"
		chars = raw_input()

def tweetIt(message):
	if(checkChars(message) == True):
		api.update_status(message)

def retweetIt(username):
	for status in api.user_timeline("@"+username):
		api.retweet(status.id)
		addDelay()
		#Ask for how many tweets they want to retweet

def replyById(tweet_id,username,message):
	if(checkChars(message) == True):
		username = "@"+username
		api.update_status(username+message,tweet_id)

def replyToWordInMyTimeLine(word):
	myTweets = api.home_timeline()
	for tweet in myTweets:
		if word in tweet.text:
			api.update_status("thanks!")
			addDelay()

def sendDirectMessage(username,message):
	if(checkChars(message) == True):
		api.send_direct_message(screen_name=username,text=message)

def listAllFollowes(username):
	for user in tweepy.Cursor(api.followers,screen_name=username).items():
		print user.screen_name
		addDelay()
#		print user.id

def printUserTweets(username):
	print "Here are the 20 latest tweets (if there are any or 20)"
	print " "
	for tweets in api.user_timeline(screen_name=username,count=20):
		print tweets.text
		addDelay()
	print " "

