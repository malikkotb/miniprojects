from pprint import pprint
import requests

# NBA stats endpoint
endpoint = "https://data.nba.net"

def getLinks():
    url_links = "https://data.nba.net/prod/v1/today.json"
    data = requests.get(url_links).json()
    links = data["links"]
    return links


# Current Scoreboard
def get_scoreboard():
    scoreboard = getLinks()['currentScoreboard']
    data = requests.get(endpoint+scoreboard).json()['games']
    for game in data:
        #pprint(game.keys())
        home_team = game['hTeam']
        visitor_team = game['vTeam']
        period = game["period"]['current']
        clock = game["clock"]
        print("------------------------------------------------")
        print(f"{home_team['triCode']} - {visitor_team['triCode']}")

        print(f"{home_team['score']} - {visitor_team['score']}")


def getStandings():
    standings = getLinks()['leagueConfStandings']
    data = requests.get(endpoint+standings).json()['league']['standard']['conference']
    print("Eastern Conference:")
    for team in data['east']:
        print(team["teamSitesOnly"]["teamNickname"])
    print("---------------------------------------------")
    print("Western Conference:")
    for team in data['east']:
        print(team["teamSitesOnly"]["teamNickname"])


getStandings()