import constants.constants as constants
import json
import re
import sys

round = sys.argv[1]
if not round:
   round = 0
   print("Parsing Round 0 data. To parse other data, provide the round as a script parameter.")

IMPORT_FILE = re.sub(
    "imports/import",
    f"imports/{constants.YEAR}/import",
   constants.PLAYER_STATS_IMPORT[f"IMPORT_PLAYER_STATS_R{round}"]
)

OUTPUT_FILE = re.sub(
    "outputs/output",
    f"outputs/{constants.YEAR}/output",
   constants.PLAYER_STATS_OUTPUT[f"JSON_PLAYER_STATS_R{round}"]
)

# INSTRUCTIONS:
# 1. Open your Browser, open the Inspector and select the Network Tab
# 2. Navigate to the NRL Super Coach website and login
# 3. Search for 'https://www.supercoach.com.au/2025/api/nrl/classic/v1/players-cf' in the captured calls
# 4. Copy+Paste the response data into the appropriate location eg: 'constants.IMPORT_PLAYER_STATS_R0'
# 5. This flow will then be functional
with open(IMPORT_FILE) as f:
    player_stats_data = json.load(f)
    if player_stats_data: print("Loaded data successfully.")
    else: exit("Data Failed.")

# Feels slightly cleaner to define this mapping as a class
class PlayerStatRow:
  def __init__(self, player_stat_row):
    self.stats = {
        "player_id": player_stat_row["id"],
        "last_name": player_stat_row["last_name"],
        "first_name": player_stat_row["first_name"],
        "previous_games": player_stat_row["previous_games"],
        "previous_average": player_stat_row["previous_average"],
        "previous_total": player_stat_row["previous_total"],
        "active": player_stat_row["active"],
        "team": player_stat_row["team"]["abbrev"],
        "breakeven": player_stat_row["player_stats"][0]["be1"],
        "price": player_stat_row["player_stats"][0]["price"],
        "position": player_stat_row["positions"][0]["position"],
    }

# Parse each player
parsed_stats = [ PlayerStatRow(each_player).stats for each_player in player_stats_data ]

# Store them in a JSON file
with open(OUTPUT_FILE, 'w') as file_output:
    json.dump(parsed_stats, file_output)
