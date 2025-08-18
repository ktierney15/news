import requests
from datetime import datetime, timezone

class SportsNewsBase:
    """Base class for fetching and printing sports news."""

    def fetch_json(self, url: str) -> dict:
        """Helper to fetch JSON from ESPN APIs."""
        return requests.get(url).json()

class NFLNews(SportsNewsBase):
    def __init__(self, team_name: str, team_abbr: str):
        """
        team_name = display name (e.g. "Cowboys", "Patriots", "49ers")
        team_abbr = ESPN's team abbreviation (e.g. "dal", "ne", "sf")
        """
        self.team_name = team_name
        self.team_abbr = team_abbr

        self.scoreboard_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
        self.record_url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{self.team_abbr}"
        self.news_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/news"

    def print_latest_game(self):
        scoreboard = self.fetch_json(self.scoreboard_url)
        game = None

        for event in scoreboard["events"]:
            for comp in event["competitions"][0]["competitors"]:
                if comp["team"]["name"] == self.team_name:
                    game = event
                    break

        if game:
            teams = game["competitions"][0]["competitors"]
            print(f"Last {self.team_name} Game:")
            for t in teams:
                print(f"{t['team']['displayName']} {t['score']} {'(W)' if t.get('winner') else ''}")
            print(f"Status: {game['competitions'][0]['status']['type']['description']}\n")

    def print_record(self):
        record_data = self.fetch_json(self.record_url)
        record_summary = record_data["team"]["record"]["items"][0]["summary"]
        print(f"{self.team_name} Record: {record_summary}\n")

    def print_news(self):
        news_data = self.fetch_json(self.news_url)
        print("NFL News:")
        for i, article in enumerate(news_data.get("articles", []), 1):
            title = article.get("headline")
            link = article.get("links", {}).get("web", {}).get("href")
            print(f"{i}. {title} - {link}")
        print()

    def display(self):
        self.print_latest_game()
        self.print_record()
        self.print_news()


class UFCNews(SportsNewsBase):
    def __init__(self):
        self.scoreboard_url = "https://site.api.espn.com/apis/site/v2/sports/mma/ufc/scoreboard"
        self.news_url = "https://site.api.espn.com/apis/site/v2/sports/mma/ufc/news"

    def print_events(self):
        data = self.fetch_json(self.scoreboard_url)
        calendar = data['leagues'][0]['calendar']
        now = datetime.now(timezone.utc)

        past_events, next_event = [], None

        for event in calendar:
            start = datetime.fromisoformat(event['startDate'].replace("Z", "+00:00"))
            if start < now:
                past_events.append(event)
            elif not next_event:
                next_event = event

        print("Previous UFC Event:")
        for e in past_events[-1:]:
            print(f"- {e['label']} | {e['startDate']} | Event API: {e['event']['$ref']}")

        if next_event:
            print("\nNext UFC Event:")
            print(f"- {next_event['label']} | {next_event['startDate']} | Event API: {next_event['event']['$ref']}")
        else:
            print("\nNo upcoming UFC events found.")

    def print_news(self):
        news_data = self.fetch_json(self.news_url)
        print("\nUFC News:")
        for i, article in enumerate(news_data.get("articles", []), 1):
            title = article.get("headline")
            link = article.get("links", {}).get("web", {}).get("href")
            print(f"{i}. {title} - {link}")
        print()

    def display(self):
        self.print_events()
        self.print_news()



class EPLNews(SportsNewsBase):
    def __init__(self):
        self.scoreboard_url = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard"
        self.news_url = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/news"

    def print_matches(self):
        data = self.fetch_json(self.scoreboard_url)
        print(f"Today's EPL Matches ({datetime.utcnow().date()}):")

        for event in data.get("events", []):
            comps = event["competitions"][0]["competitors"]
            match_name = " vs ".join([c["team"]["displayName"] for c in comps])
            print(f"- {match_name}")

            for c in comps:
                team_name = c["team"]["displayName"]
                team_id = c["team"]["id"]
                team_link = f"https://www.espn.com/soccer/team/_/id/{team_id}"
                print(f"    {team_name} standings link: {team_link}")
            print()

    def print_news(self):
        news_data = self.fetch_json(self.news_url)
        print("EPL News:")
        for i, article in enumerate(news_data.get("articles", []), 1):
            title = article.get("headline")
            link = article.get("links", {}).get("web", {}).get("href")
            print(f"{i}. {title} - {link}")
        print()

    def display(self):
        self.print_matches()
        self.print_news()


class SportsNews:
    """Main orchestrator to fetch all sports news."""

    def __init__(self, nfl_team_name: str, nfl_team_abbr: str):
        # NFL requires a favorite team
        self.nfl = NFLNews(team_name=nfl_team_name, team_abbr=nfl_team_abbr)

        # These don’t need parameters yet
        self.ufc = UFCNews()
        self.epl = EPLNews()

    def display_all(self):
        print("\nNFL:")
        self.nfl.display()

        print("\nEPL:")
        self.epl.display()

        print("\nUFC:")
        self.ufc.display()

