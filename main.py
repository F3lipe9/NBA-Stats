import pandas as pd

playoffs = pd.read_csv("play_off_totals_2010_2024.csv")

# print(playoffs)

regularSeason = pd.read_csv("regular_season_totals_2010_2024.csv")

# print(regularSeason)

fullSeason = pd.concat([regularSeason, playoffs])

# print(fullSeason)

# Clean Data

fullSeason = fullSeason.drop(columns=["GP_RANK" ,"W_RANK","L_RANK","W_PCT_RANK","MIN_RANK","FGM_RANK",
                                      "FGA_RANK","FG_PCT_RANK","FG3M_RANK","FG3A_RANK","FG3_PCT_RANK",
                                      "FTM_RANK","FTA_RANK", "FT_PCT_RANK","OREB_RANK","DREB_RANK",
                                      "REB_RANK","AST_RANK","TOV_RANK","STL_RANK","BLK_RANK",
                                      "BLKA_RANK","PF_RANK","PFD_RANK","PTS_RANK","PLUS_MINUS_RANK",
                                        "TEAM_ID", "GAME_ID", "GAME_DATE", "MATCHUP","AVAILABLE_FLAG"])

print(fullSeason.groupby(["TEAM_ABBREVIATION"]).sum(["PTS"]))