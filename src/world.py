import feedparser
from datetime import datetime, timezone

class GetNews:
    def __init__(self, feed_url, name, category):
        self.feed_url = feed_url
        self.name = name
        self.category = category

    def get_todays_news(self):
        feed = feedparser.parse(self.feed_url)
        today = datetime.now(timezone.utc).date()
        out = []
        
        for entry in feed.entries:
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            
            if published.date() == today:
                title = entry.get("title")
                link = entry.get("link")
                out.append([title, link])
        return out
    
    def print_todays_news(self):
        news = self.get_todays_news()
        
        print(f"\n{self.category} ({self.name}):")
        if news:
            count = 0
            for item in news:
                count += 1
                print(f"{count}. {item[0]} - {item[1]}")
        else:
            print(f"No {self.name} published today.")
            
class WorldNews:
    def __init__(self):
        self.epoch = GetNews(feed_url="https://feed.theepochtimes.com/us/us-politics/feed", name="Epoch News", category="US Politics")
        self.bbc = GetNews(feed_url="https://feeds.bbci.co.uk/news/world/rss.xml", name="BBC News", category="Global Politics")

    def display_all(self):        
        self.epoch.print_todays_news()
        self.bbc.print_todays_news()
