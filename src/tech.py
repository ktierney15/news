import requests
from utils import hyperlink


class TechNewsBase:
    """Base class for fetching and printing tech news."""

    def fetch_json(self, url: str) -> dict:
        """Helper to fetch JSON from APIs."""
        return requests.get(url).json()
    
class HackerNews(TechNewsBase):
    def __init__(self, story_count: int):
        self.url="https://hacker-news.firebaseio.com/v0/topstories.json"
        self.story_count = story_count

    def get_news(self):
        news_data = self.fetch_json(self.url)
        top_stories = []

        for story in range(self.story_count):
            story_id = news_data[story]
            response = requests.get(
                url=f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            )
            item = response.json()
            s = {
                "by" : item["by"],
                "title" : item["title"],
                "url" : item["url"]

            }
            top_stories.append(s)
        return top_stories
    
    def print_news(self):
        news = self.get_news()
        print("\nY Combinator:")
        for i, story in enumerate(news):
            print(f"{i+1}. {hyperlink(story['url'], story['title'])}")

class TechCrunch(TechNewsBase):
    def __init__(self, story_count: int):
        self.url=f"https://techcrunch.com/wp-json/wp/v2/posts?per_page={story_count}"

    def get_news(self):
        news_data = self.fetch_json(self.url)
        top_stories = []

        for article in news_data:
            a = {
                "title": article['title']['rendered'],
                "link": article['link'],
                "date": article['date']
            }
            top_stories.append(a)
    
        return top_stories
    
    def print_news(self):
        news = self.get_news()
        print("\nTech Crunch:")
        for i, article in enumerate(news):
            print(f"{i+1}. {hyperlink(article['link'], article['title'])}\nPublished: {article['date']}")

class TechNews:
    """Main orchestrator to fetch all tech news."""

    def __init__(self, story_count: int):
        self.hacker_news = HackerNews(story_count=story_count)
        self.tech_crunch = TechCrunch(story_count=story_count)

    def display_all(self):
        self.hacker_news.print_news()
        self.tech_crunch.print_news()