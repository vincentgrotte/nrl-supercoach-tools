import constants.constants as constants
import json
import re
import sys

SEP_CHAR = "\t"

round = sys.argv[1]
if not round:
   round = 0
   print("Using Round 0 data. To use other data, provide the round as a script parameter.")

INPUT_FILE = re.sub(
    "outputs/output",
    f"outputs/{constants.YEAR}/output",
   constants.PLAYER_STATS_OUTPUT[f"JSON_PLAYER_STATS_R{round}"]
)

with open(INPUT_FILE) as f:
    player_data = json.load(f)
    if player_data: print("Loaded data successfully.")
    else: exit("Load player data Failed.")

with open(constants.PLAYERS_ENRICHED_SHEET, '+w') as f:

    # Construct header row

    headers_output_string = \
        f"player_id{SEP_CHAR}" \
        f"last_name{SEP_CHAR}" \
        f"first_name{SEP_CHAR}" \
        f"previous_games{SEP_CHAR}" \
        f"previous_average{SEP_CHAR}" \
        f"previous_total{SEP_CHAR}" \
        f"active{SEP_CHAR}" \
        f"team{SEP_CHAR}" \
        f"breakeven{SEP_CHAR}" \
        f"price{SEP_CHAR}" \
        f"position{SEP_CHAR}" \
        f"\n"

    f.write(headers_output_string)

    # Construct rows

    for player in player_data:

        player_output_string = \
            f"{player["player_id"]}{SEP_CHAR}" \
            f"{player["last_name"]}{SEP_CHAR}" \
            f"{player["first_name"]}{SEP_CHAR}" \
            f"{player["previous_games"]}{SEP_CHAR}" \
            f"{player["previous_average"]}{SEP_CHAR}" \
            f"{player["previous_total"]}{SEP_CHAR}" \
            f"{player["active"]}{SEP_CHAR}" \
            f"{player["team"]}{SEP_CHAR}" \
            f"{player["breakeven"]}{SEP_CHAR}" \
            f"{player["price"]}{SEP_CHAR}" \
            f"{player["position"]}{SEP_CHAR}" \
            f"\n"
        
        f.write(player_output_string)

