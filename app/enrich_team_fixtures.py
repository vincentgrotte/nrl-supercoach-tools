import constants.constants as constants
import json

# INSTRUCTIONS:
# The logic in this script depends on the successful execution of:
# 1. parse_and_store_player_stats.py
# 2. fetch_team_fixtures.py

with open(constants.TEAM_FIXTURES) as f:
    team_fixtures_data = json.load(f)
    if team_fixtures_data: print("Loaded data successfully.")
    else: exit("Team fixtures data Failed.")

class ScheduledRound:
    def __init__(self, round, opp):
        self.stats = {
            "is_bye": True if not opp else False,
            "is_origin": True if round in constants.ORIGIN_ROUNDS else False,
            "opp": opp,
            "round": round,
        }
        
team_schedules = {}

for team, schedule in team_fixtures_data.items():

    scheduled_matches = {
        match["round"]: match["opp"] for match in schedule
    }

    enriched_schedule = {
        round: ScheduledRound(round, scheduled_matches.get(round)).stats
        for round in range(1, constants.TOTAL_ROUNDS + 1)
    }

    team_byes = [
        round for round in range(1, constants.TOTAL_ROUNDS + 1)
        if enriched_schedule[round]['is_bye'] == True
    ]

    # team_byes_formatted_with_asterisk_for_origin = [
    #      ( str(bye) + "*" if bye in [12, 15, 18] else bye ) for bye in team_byes 
    # ]

    gap_between_r0_b1 = team_byes[0] - 1
    gap_between_b1_b2 = team_byes[1] - team_byes[0]
    gap_between_b2_b3 = team_byes[2] - team_byes[1]
    gap_between_b3_and_end = constants.TOTAL_ROUNDS - team_byes[2]
    total_gap_length = gap_between_r0_b1 + gap_between_b1_b2 + gap_between_b2_b3

    team_schedules[team] = {
        "byes": team_byes,
        "gap_between_r0_b1": gap_between_r0_b1,
        "gap_between_b1_b2": gap_between_b1_b2,
        "gap_between_b2_b3": gap_between_b2_b3,
        "gap_between_b3_and_end": gap_between_b3_and_end,
        "total_gap_length": total_gap_length,
        "schedule": enriched_schedule
    }

with open(constants.TEAM_FIXTURES_ENRICHED, 'w') as file_output:
    json.dump(team_schedules, file_output)



