import json

CURRENT_ROUND = 1
ORIGIN_ROUNDS = [12, 15, 18]

FILE = "byes.json"
# Create text file to store NRL stats
with open(FILE) as f:
    data = json.load(f)
    if data: print("Loaded data successfully.")
    else: exit("Data Failed.")

team_byes = {}

for bye_round in data:
    round = bye_round["round"]
    
    for team in bye_round["teams"]:
        if not team_byes.get(team):
            team_byes[team] = [round]
        else:
            team_byes[team] += [round]

teams_with_latest_byes = []

biggest_gaps = []
team_gaps = {}

for team in team_byes:
    # print(team, team_byes[team])
    byes = team_byes[team]
    gap_between_r0_b1 = byes[0] - 1
    gap_between_b1_b2 = byes[1] - byes[0]
    gap_between_b2_b3 = byes[2] - byes[1]
    gap_between_b3_r27 = 27 - byes[2]
    # gap_between_b1_b3 = byes[2] - byes[0]

    team_gaps[team] = (
        team,
        gap_between_r0_b1 + gap_between_b1_b2 + gap_between_b2_b3,
        gap_between_r0_b1,
        gap_between_b1_b2,
        gap_between_b2_b3,
        "(" + str(gap_between_b3_r27) + ")",
        ((gap_between_r0_b1 + gap_between_b1_b2 + gap_between_b2_b3) // 3),
        [ ( str(bye) + "*" if bye in [12, 15, 18] else bye ) for bye in byes ],
        # gap_between_b1_b3
    )

# print(team_gaps)

# team_gaps_between_r0_b1 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[2], reverse=True)
# pprint.pp(team_gaps_between_r0_b1)
# team_gaps_between_b1_b2 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[3], reverse=True)
# pprint.pp(team_gaps_between_b1_b2)
# team_gaps_between_b2_b3 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[4], reverse=True)
# pprint.pp(team_gaps_between_b2_b3)
team_gaps_between_b2_b3 = sorted(team_gaps.values(), 
                                key=lambda tup: tup[len(tup)-2],
                                reverse=True)


# for team in team_byes:
#     # print(team, team_byes[team])
#     byes = team_byes[team]
#     gap_between_r1_b1 = byes[0] - 1
#     gap_between_b1_b2 = byes[1] - byes[0]
#     gap_between_b2_b3 = byes[2] - byes[1]
#     # gap_between_b1_b3 = byes[2] - byes[0]

#     team_gaps[team] = (
#         team,
#         "B:" + \
#         str([ ( str(bye) + "*" if bye in [12, 15, 18] else bye ) for bye in byes ]),
#         "T:" + \
#         str(gap_between_r1_b1 + gap_between_b1_b2 + gap_between_b2_b3),
#         "R1-B1:" + str(gap_between_r1_b1),
#         "B1-B2:" + str(gap_between_b1_b2),
#         "B2-B3:" + str(gap_between_b2_b3),
#         "A:" + str(
#             (gap_between_r1_b1 + gap_between_b1_b2 + gap_between_b2_b3) // 3
#         )
#         # gap_between_b1_b3
#     )

# print(team_gaps)

# team_gaps_between_r0_b1 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[2], reverse=True)
# pprint.pp(team_gaps_between_r0_b1)
# team_gaps_between_b1_b2 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[3], reverse=True)
# pprint.pp(team_gaps_between_b1_b2)
# team_gaps_between_b2_b3 = sorted(team_gaps.values(), key=lambda gaps_tuple: gaps_tuple[4], reverse=True)
# pprint.pp(team_gaps_between_b2_b3)

# team_gaps_between_b2_b3 = sorted(team_gaps.values(), key=lambda tup: tup[len(tup)-1],reverse=True)
# pprint.pp(team_gaps_between_b2_b3)


[ print(team_info) for team_info in team_gaps_between_b2_b3 ]