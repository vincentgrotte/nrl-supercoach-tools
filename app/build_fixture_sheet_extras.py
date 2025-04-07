import app.lib.constants as constants
import json

SEP_CHAR = "\t"

with open(constants.TEAM_FIXTURES_ENRICHED) as f:
    team_fixtures_data = json.load(f)
    if team_fixtures_data: print("Loaded data successfully.")
    else: exit("Team fixtures enriched data Failed.")

with open(constants.TEAM_FIXTURES_GRID_SHEET, '+w') as f:

    # Construct header row

    headers_output_string = f"team{SEP_CHAR}"

    for round in range(1, constants.TOTAL_ROUNDS + 1):
        headers_output_string += f"{round}{SEP_CHAR}"

    headers_output_string += f"BYEs\t"
    headers_output_string += f"R0-B1\t"
    headers_output_string += f"B1-B2\t"
    headers_output_string += f"B2-B3\t"
    headers_output_string += f"B3-END\t"
    headers_output_string += f"TOTAL_GAP\t"

    headers_output_string += "\n"

    f.write(headers_output_string)

    # Construct rows

    for team, fixture_data in team_fixtures_data.items():
        
        team_schedule_output_string = f"{team}{SEP_CHAR}"

        for match in fixture_data['schedule'].values():
            schedule_value = match.get('opp')
            round = match.get('round')
            if not schedule_value: schedule_value = "BYE"
            team_schedule_output_string += f"{schedule_value}{SEP_CHAR}"

        team_schedule_output_string += f"{fixture_data['byes']}\t"
        team_schedule_output_string += f"{fixture_data['gap_between_r0_b1']}\t"
        team_schedule_output_string += f"{fixture_data['gap_between_b1_b2']}\t"
        team_schedule_output_string += f"{fixture_data['gap_between_b2_b3']}\t"
        team_schedule_output_string += f"{fixture_data['gap_between_b3_and_end']}\t"
        team_schedule_output_string += f"{fixture_data['total_gap_length']}\t"
        
        team_schedule_output_string += "\n"
        
        f.write(team_schedule_output_string)

