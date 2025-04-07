from app.lib.utilities import get_round, get_player_stats_path
from app.data_types.player_stats import PlayerStatRow
import app.lib.constants as constants
import json


round = get_round()
IMPORT_FILE = get_player_stats_path("import", constants.YEAR, round, ".json")
OUTPUT_FILE = get_player_stats_path("output", constants.YEAR, round, ".json")

# INSTRUCTIONS:
# 1. Open your Browser, open the Inspector and select the Network Tab
# 2. Navigate to the NRL Super Coach website and login
# 3. Search for 'players-cf' in the captured calls
# 4. Copy+Paste the response data into the appropriate location eg: 'constants.IMPORT_PLAYER_STATS_R0'
# 5. This flow will then be functional
with open(IMPORT_FILE) as f:
    player_stats_data = json.load(f)
    if player_stats_data: print("Loaded data successfully.")
    else: exit("Data Failed.")

# Parse each player
parsed_stats = [ PlayerStatRow(each_player).stats for each_player in player_stats_data ]

# Store them in a JSON file
with open(OUTPUT_FILE, 'w') as file_output:
    json.dump(parsed_stats, file_output)


