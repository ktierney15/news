import json
import click

from . import tech, sports, weather, world



def generate_news_summary():
    """Aggregates news topics that you like and return output"""
    # Weather
    print("-------------------------------------------")
    print("                 WEATHER")
    print("-------------------------------------------")
    current_weather = weather.WeatherData(longitude=-74.0, latitude=40.7) # NYC
    current_weather.print_current_weather()

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


    # World News
    print("-------------------------------------------")
    print("                 World")
    print("-------------------------------------------")
    world_news = world.WorldNews()
    world_news.display_all()
    pass


@click.command()

def main():
    ''' Entrypoint for CLI tool '''


    generate_news_summary()


if __name__ == "__main__":
    main()