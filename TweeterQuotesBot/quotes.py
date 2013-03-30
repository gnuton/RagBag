#
# Copyright (c) 2013 Antonio "GNUton" Aloisio
#
# This file has been downloaded from https://github.com/gnuton/RagBag
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import feedparser
from HTMLParser import HTMLParser
import tweepy
import re
import sys

# --- V A R S ---
#rssUrl="http://pipes.yahoo.com/pipes/pipe.run?_id=6h6J2j0_3RGUoYItnkartA&_render=rss"
rssUrl="http://it.wikiquote.org/w/api.php?action=featuredfeed&feed=qotd"

# These vars were used with old authentication method
#username="BOT_TWITTER_USERNAME"
#password="BOT_TWITTER_PASSWORD"

consumer_token="YOUR_CONSUMER_TOKEN"
consumer_secret="YOUR_CONSUMER_SECRET"
access_key="YOUR_ACCESS_KEY"
access_secret="YOUR_ACCESS_SECRET"

# --- U t i l s ---
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def sendTweet(text):
    # Old auth method replaced by the lines below
    # auth = tweepy.BasicAuthHandler(username, password)

    # new auth method
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Update Twitter status
    try:   
        api.update_status(text)
    except tweepy.TweepError, e:
        print 'Failed to update! %s' % e
        return False
    return True

# --- C O D E ---
if __name__ == "__main__":
    print "Downloading RSS"
    feed = feedparser.parse(rssUrl)
    print "RSS contains %s items" % str(len(feed["items"])) 

    for item in reversed(feed["items"]): 
	# Get and sanitize text to tweet
	text=strip_tags(item["description"])
	print "Text length is:" + str(len(text))
	text = re.sub('\|','', text)
	text = re.sub(' +',' ', text)
       
        # Uncomment the line below to truncate the RSS entry to 140 chars
	#text=text[:140]

	print "Tweeting" + text.encode("utf8")
	if len(text) > 140:
		continue
	if sendTweet(text) == True:
		sys.exit(0)
