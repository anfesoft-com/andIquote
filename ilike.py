import requests
from requests.exceptions import HTTPError


url = "https://api.twitter.com/2/users/1503277190963683328/liked_tweets"
bearer = "YOURBEARERCODEHERE"

payload={}
headers = {
  'Authorization': 'Bearer '+bearer
}


f = open("likepool.txt", "a")


response = requests.request("GET", url, headers=headers, data=payload)
response.raise_for_status()
jsonResponse = response.json()
for x in jsonResponse['data']:
    f.write(x['id']+'\n')
