import constants.constants as constants
import json

SEP_CHAR = "\t"

with open(constants.TEAM_FIXTURES_ENRICHED) as f:
    team_fixtures_data = json.load(f)
    if team_fixtures_data: print("Loaded data successfully.")
    else: exit("Team fixtures enriched data Failed.")

with open(constants.TEAM_FIXTURES_GRID_SHEET, '+w') as f:

    headers_output_string = f"team{SEP_CHAR}"

    for round in range(1, constants.TOTAL_ROUNDS + 1):
        headers_output_string += f"{round}{SEP_CHAR}"

    headers_output_string += "\n"

    f.write(headers_output_string)

    for team, schedule in team_fixtures_data.items():
        
        team_schedule_output_string = f"{team}{SEP_CHAR}"

        for match in schedule.values():
            schedule_value = match.get('opp')
            round = match.get('round')
            if not schedule_value: schedule_value = "BYE"
            team_schedule_output_string += f"{schedule_value}{SEP_CHAR}"
        
        team_schedule_output_string += "\n"
        
        f.write(team_schedule_output_string)

