from app.lib.utilities import get_round, get_player_stats_path
import app.lib.constants as constants
import json


SEP_CHAR = "\t"

round = get_round()
INPUT_FILE = get_player_stats_path("output", constants.YEAR, round, ".json")
OUTPUT_FILE = get_player_stats_path("enriched", constants.YEAR, round, ".csv")

with open(INPUT_FILE) as f:
    player_data = json.load(f)
    if player_data: print("Loaded data successfully.")
    else: exit("Load player data Failed.")

with open(OUTPUT_FILE, '+w') as f:

    # Construct header row

    headers_output_string = \
        f"player_id{SEP_CHAR}" \
        f"last_name{SEP_CHAR}" \
        f"first_name{SEP_CHAR}" \
        f"team{SEP_CHAR}" \
        f"position{SEP_CHAR}" \
        f"total_games{SEP_CHAR}" \
        f"total_score{SEP_CHAR}" \
        f"average_score{SEP_CHAR}" \
        f"price{SEP_CHAR}" \
        f"breakeven{SEP_CHAR}" \
        f"projected_score{SEP_CHAR}" \
        f"projected_price{SEP_CHAR}" \
        f"projected_price_change{SEP_CHAR}" \
        f"active{SEP_CHAR}" \
        f"\n"

    f.write(headers_output_string)

    # Construct rows

    for player in player_data:

        projected_price_change = player["projected_price"] - player["price"]

        player_output_string = \
            f"{player["player_id"]}{SEP_CHAR}" \
            f"{player["last_name"]}{SEP_CHAR}" \
            f"{player["first_name"]}{SEP_CHAR}" \
            f"{player["team"]}{SEP_CHAR}" \
            f"{player["position"]}{SEP_CHAR}" \
            f"{player["total_games"]}{SEP_CHAR}" \
            f"{player["total_score"]}{SEP_CHAR}" \
            f"{player["average_score"]}{SEP_CHAR}" \
            f"{player["price"]}{SEP_CHAR}" \
            f"{player["breakeven"]}{SEP_CHAR}" \
            f"{player["projected_score"]}{SEP_CHAR}" \
            f"{player["projected_price"]}{SEP_CHAR}" \
            f"{projected_price_change}{SEP_CHAR}" \
            f"{player["active"]}{SEP_CHAR}" \
            f"\n"
        
        f.write(player_output_string)

