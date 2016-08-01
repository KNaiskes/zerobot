################################################################
#Creator : Kiriakos Naiskes
#Contact me at : kiriakosnaiskes@gmail.com
################################################################

import tweepy
import time
import argparse
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
	if(len(chars) > 140):
		print "Your text must be equal to 140 or less characters. Aborted"
		return False
	return True

def tweetIt():
	print ("Enter your tweet: ")
	message = raw_input()
	if(checkChars(message) == True):
		api.update_status(message)

def retweetIt():
	print ("Enter username :")
	username = raw_input()
	for status in api.user_timeline("@"+username):
		api.retweet(status.id)
		addDelay()
		#Ask for how many tweets they want to retweet

def replyById():
	print("Enter tweet's id :")
	tweet_id = raw_input()
	print("Enter username :")
	username = raw_input()
	print("Enter your message :")
	message = raw_input()
	if(checkChars(message) == True):
		username = "@"+username
		api.update_status(username+message,tweet_id)

def replyToWordInMyTimeLine():
	print("Enter the word you are looking for :")
	word = raw_input()
	print("Enter your answer : ")
	answer = raw_input()
	myTweets = api.home_timeline()
	if(checkChars(answer) == True):
		for tweet in myTweets:
			if word in tweet.text:
				api.update_status(answer)
				addDelay()

def sendDirectMessage():
	print("Enter user's name who you want to send a direct message :")
	username = raw_input()
	print("Enter the message : ")
	message = raw_input()
	if(checkChars(message) == True):
		api.send_direct_message(screen_name=username,text=message)

def listAllFollowes():
	print("Which user's followers do you want to list ? :")
	username = raw_input()
	for user in tweepy.Cursor(api.followers,screen_name=username).items():
		print user.screen_name
		addDelay()
#		print user.id

def printUserTweets():
	print("Whose user do you want to list their tweets ? :")
	username = raw_input()
	print "Here are the 20 latest tweets (if there are any or 20)"
	print " "
	for tweets in api.user_timeline(screen_name=username,count=20):
		print tweets.text
		addDelay()
	print " "

def menu():
	print """
	#############################################################################
	# 			Options                                             #
        #                                                                           #
	#		1) -pt post a tweet			                    #
	#		2) -rt retweet 				                    #
	#	        3) -rbw reply based to a specifi word	                    #
	#		4) -dm send a direct message	                            #
	#		5) -lf list all followers of a user	                    #
	#               6) -gt print the latest 20 tweets of a user                 #
	#                                                                           #
	#############################################################################
	"""


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-pt","--posttweet",help="post a tweet",action="store_true")
	parser.add_argument("-rt","--retweet",help="retweet posts by user",action="store_true")
	parser.add_argument("-rbw","--replybyword",help="reply based to a specifi word",action="store_true")
	parser.add_argument("-dm","--directmessage",help="send a direct message",action="store_true")
	parser.add_argument("-lf","--listfollowers",help="list followers",action="store_true")
	parser.add_argument("-gt","--gettweets",help="get user tweets",action="store_true")
	args = parser.parse_args()

	if args.posttweet:
		tweetIt()
	elif args.retweet:
		retweetIt()
	elif args.replybyword:
		replyToWordInMyTimeLine()
	elif args.directmessage:
		sendDirectMessage()
	elif args.listfollowers:
		listAllFollowes()
	elif args.gettweets:
		printUserTweets()
	else:
		menu()

main()

print " "
print "Done"

