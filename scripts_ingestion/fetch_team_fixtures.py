import constants.constants as constants
import curl_commands.team_fixtures as fetch_team_fixtures
import json
import pprint
import subprocess
import re

# INSTRUCTIONS
# 1. Open your Browser, open the Inspector and select the Network Tab
# 2. Navigate to the NRL Super Coach website and login
# 3. Navigate to 'My Team', and click any player, and select 'Season Stats'
# 3. Search for 'upcoming_fixtures' in the captured calls
# 4. Copy+paste the whole curl command into curl_commands.team_fixtures
# 5. This flow will then be functional

def get_fixtures(
    player_id,
    team,
):
    print(f"# Fetching fixture stats for {team}")

    command = re.sub(
        r"players/.*/upcoming_fixture",
        f"players/{player_id}/upcoming_fixture",
        fetch_team_fixtures.CURL_TO_FETCH_TEAM_FIXTURES
    )

    fixture_results = subprocess.run([command], capture_output=True, text=True, shell=True)

    json_fixtures = json.loads(fixture_results.stdout)

    team_fixtures = [
        {
            "opp": item['opp']['abbrev'],
            "round": item['round']
        } for item in json_fixtures
    ]

    return team_fixtures

with open(constants.JSON_PLAYER_STATS_R0) as f:
    player_stats_data = json.load(f)
    if player_stats_data: print("Loaded player stats data successfully.")
    else: exit("Player stats data Failed.")
    
player_from_each_team = {}

for player in player_stats_data:
    player_team = player['team']

    if not player['position'] == 'FLB':
        continue

    if player_team not in player_from_each_team:
        player_from_each_team[player_team] = {
            'id': player['player_id'],
            'name': f"{player['first_name']} {player['last_name']}",
            'team': player_team
        }
        
    if len(player_from_each_team) == 17:
        break

team_fixtures = {}

for player in player_from_each_team.values():
    team = player['team']
    if team not in team_fixtures:
        team_fixtures[team] = get_fixtures(player['id'], team)

with open(constants.TEAM_FIXTURES, 'w') as file_output:
    json.dump(team_fixtures, file_output)
