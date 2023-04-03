import praw
import config
import time
import os

def redditbot_login():
	print ("Logging in now")
	reddit = praw.Reddit(yourusername = config.yourusername,
				yourpassword = config.yourpassword,
				client_id = config.client_id,
				client_secret = config.client_secret,
				reddituser_agent = "The Reddit Commenter v1.0")
	print ("You're logged in!")

	return reddit

def run_bot(reddit, comments):
	print ("Searching last 1,000 comments")

	for comments in reddit.subreddit('test').comments(limit=1000):
		if "user comment" in comments.body and comments.id not in comments and comments.author != reddit.user.me():
			print ("String with \"user comment\" found in comment ") + comments.id
			comments.reply("I completely agree with you!")
			print ("Replied to comment ") + comments.id

			comments.append(comments.id)

			with open ("comments", "a") as f:
				f.write(comments.id + "\n")

	print ("Search Completed.")

	print ("comments_replied_to")


def get_saved_comments():
	if not os.path.isfile("comments"):
		comments = []
	else:
		with open("comments", "reddit") as f:
			comments = f.read()
			comments = comments.split("\n")
			comments = filter(None, comments)

	return comments

redditbot = redditbot_login()
comments = get_saved_comments()
print ("comments")

while True:
	run_bot(redditbot , comments)