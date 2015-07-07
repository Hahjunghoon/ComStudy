import sys
import httplib, urllib


	

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "aw1xVr4GGSRhFCZHuM1Gig7tywcyEz",
    "user": "uJm2WPxn2t6kkDZifs2j55pbMWyTXp",
    "message": "Hello World",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
