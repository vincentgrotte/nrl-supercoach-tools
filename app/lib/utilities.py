import app.lib.constants as constants
import sys


def get_path_with_year(option, year):

   return \
      f"{constants.PLAYER_STATS_FOLDER}" \
      f"{option}/{year}/{option}" \
      f"{constants.PLAYER_STATS_SUFFIX}"


def get_round():

   round = sys.argv[1]

   if not round: round = constants.DEFAULT_ROUND

   print(
      f"Parsing Round {round} data."
      f"To parse other data, provide the round as the first script parameter."
   )

   return round


def get_player_stats_path(option, year, round, file_type):

   return \
      f"{get_path_with_year(option, year)}" \
      f"{round}" \
      f"{file_type}"
   

