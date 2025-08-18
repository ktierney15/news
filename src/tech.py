import requests

def get_y_combinator_stories(stories=5):
    response = requests.get(
        url="https://hacker-news.firebaseio.com/v0/topstories.json"
    )
    
    ids = response.json()
    top_stories = []

    for story in range(stories):
        story_id = ids[story]
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

def get_techcrunch_articles(articles=5):
    response = requests.get(f"https://techcrunch.com/wp-json/wp/v2/posts?per_page={articles}")
    articles = response.json()

    top_articles = []

    for article in articles:
        a = {
            "title": article['title']['rendered'],
            "link": article['link'],
            "date": article['date']
        }
        top_articles.append(a)
   
    return top_articles
    


def get_tech_news(time_period=1):
    y_combinator_stories = get_y_combinator_stories()
    techcrunch_articles = get_techcrunch_articles()

    print("Y Combinator:")
    for i, story in enumerate(y_combinator_stories):
        print(f"{i+1}. {story['title']} - {story['url']}\n")

    print("Tech Crunch:")
    for i, article in enumerate(techcrunch_articles):
        print(f"{i+1}. {article['title']} - {article['link']}\nPublished: {article['date']}\n")

