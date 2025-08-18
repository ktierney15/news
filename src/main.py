import tech
import sports



def generate_news_summary():
    """Aggregates news topics that you like and return output"""

    # World News

    # Sports News
    print("-------------------------------------------")
    print("                 SPORTS")
    print("-------------------------------------------")
    sports_news = sports.SportsNews(nfl_team_name="Cowboys", nfl_team_abbr="dal")
    sports_news.display_all()
    
    # Tech News
    print("-------------------------------------------")
    print("                 TECH")
    print("-------------------------------------------")
    tech_news = tech.TechNews(story_count=5)
    tech_news.display_all()

    pass


def main():
    generate_news_summary()

if __name__ == "__main__":
    main()