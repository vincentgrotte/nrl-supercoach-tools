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
        "projected_score": player_stat_row["player_stats"][0]["ppts1"],
        "projected_price": player_stat_row["player_stats"][0]["pp1"],
        "price": player_stat_row["player_stats"][0]["price"],
        "position": player_stat_row["positions"][0]["position"],
        "average_score": player_stat_row["player_stats"][0]["avg3"],
        "total_games": player_stat_row["player_stats"][0]["total_games"],
        "total_score": player_stat_row["player_stats"][0]["total_points"],
    }




