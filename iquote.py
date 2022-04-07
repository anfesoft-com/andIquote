import schedule
import time
import requests
import json
import random
import string


bestandIds = 'likepool.txt'
file1 = open(bestandIds, 'r')
Lines = file1.readlines()
everyxM = 1
ln = 0


def makenonce(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    nonce = ''.join(random.choice(letters) for i in range(length))
    return nonce



def postAndQuote(ln):
	ts = int(time.time())
	nonce = makenonce(11)
	print(nonce)
	tweetid = Lines[-ln]
	cuerpo = {}
	cuerpo['text'] = "YOURTEXTHERE"
	cuerpo['quote_tweet_id'] = str(tweetid).rstrip()
	payload = json.dumps(cuerpo)
	headers = {
	'Authorization': 'OAuth oauth_consumer_key="YOURKEYHERE",oauth_token="YOURTOKENHERE",oauth_signature_method="HMAC-SHA1",oauth_timestamp="YOURTIMESTAMPHERE",oauth_nonce="YOURNONCEHERE",oauth_version="1.0",oauth_signature="YOURSIGNATUREHERE"',
	'Content-Type': 'application/json',
	'Cookie': 'guest_id=YOURCOOKIEHERE'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	print(Lines[-ln])
	


def job():
	global ln
	ln += 1
	postAndQuote(ln)
# Run job every 3 second/minute/hour/day/week,
# Starting 3 second/minute/hour/day/week from now
#schedule.every(10).seconds.do(job)
#schedule.every(everyxM).minutes.do(job)
schedule.every(1).hours.do(job)
#schedule.every(3).days.do(job)
#schedule.every(3).weeks.do(job)
# Run job every minute at the 23rd second
#schedule.every().minute.at(":23").do(job)
# Run job every hour at the 42rd minute
#schedule.every().hour.at(":42").do(job)
# Run jobs every 5th hour, 20 minutes and 30 seconds in.
# If current time is 02:00, first execution is at 06:20:30
#schedule.every(5).hours.at("20:30").do(job)
# Run job every day at specific HH:MM and next HH:MM:SS
#schedule.every().day.at("10:30").do(job)
#schedule.every().day.at("10:30:42").do(job)
# Run job on a specific day of the week
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
