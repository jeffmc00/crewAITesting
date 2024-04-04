import os
import feedparser
from datetime import datetime, timedelta


#url = "http://feeds.bbci.co.uk/news/england/rss.xml"
#url = "https://podcastfeeds.nbcnews.com/HL4TzgYC"
#url = "https://www.yahoo.com/news/rss/business/"
url = "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/business/rss.xml"
feed = feedparser.parse(url)


now = datetime.now()
time_range = timedelta(days=1)

for entry in feed.entries:
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    #print("Entry Published Date:", entry.published)
    #print("Entry Summary:", entry.summary)
    print("Entry Summary:", entry.description)
    print("\n")

for x in range(6):
    print(feed.entries[x].title)
    print("\n")