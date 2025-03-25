## Pre-requisite Manual Work

### fetch_team_fixtures.py

python3 -m scripts_ingestion.fetch_team_fixtures

A curl command to get all of the upcoming fixtures for each team.

1. Open your Browser, open the Inspector and select the Network Tab
2. Navigate to the NRL Super Coach website and login
3. Navigate to 'My Team', and click any player, and select 'Season Stats'
3. Search for 'upcoming_fixtures' in the captured calls
4. Find the Authorization and Cookie headers
5. Copy+paste those values into config_and_constants/auth_config
6. This flow will then be functional and will output a json document with all of the players' stats

### parse_and_store_player_stats.py

python3 -m scripts_ingestion.parse_and_store_player_stats

A script to run on data taken manually from the NRL Supercoach website to get specific player

1. Open your Browser, open the Inspector and select the Network Tab
2. Navigate to the NRL Super Coach website and login
3. Search for 'https://www.supercoach.com.au/2025/api/nrl/classic/v1/players-cf' in the captured calls
4. Copy+Paste the response data into the appropriate location eg: 'constants.IMPORT_PLAYER_STATS_R0'
5. This flow will then be functional and will output a json document with each team's fixtures

## Functionality dependent on the previous steps

### enrich_team_fixtures.py

python3 -m scripts_ingestion.enrich_team_fixtures

1. Produce a json document with the scraped fixture data transformed into a more workable format

### build_fixture_grid_spreadsheet.py

python3 -m scripts_sheets.build_fixture_sheet

1. Produce a csv document with the fixtures of team compared as a grid
