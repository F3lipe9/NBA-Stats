import pandas as pd

# Create Data and Merge to create one DataFrame

playoffs = pd.read_csv("play_off_totals_2010_2024.csv")

regularSeason = pd.read_csv("regular_season_totals_2010_2024.csv")

fullSeason = pd.concat([regularSeason, playoffs])

# Clean Data

fullSeason = fullSeason.drop(columns=["GP_RANK" ,"W_RANK","L_RANK","W_PCT_RANK","MIN_RANK","FGM_RANK",
                                      "FGA_RANK","FG_PCT_RANK","FG3M_RANK","FG3A_RANK","FG3_PCT_RANK",
                                      "FTM_RANK","FTA_RANK", "FT_PCT_RANK","OREB_RANK","DREB_RANK",
                                      "REB_RANK","AST_RANK","TOV_RANK","STL_RANK","BLK_RANK",
                                      "BLKA_RANK","PF_RANK","PFD_RANK","PTS_RANK","PLUS_MINUS_RANK",
                                        "TEAM_ID", "GAME_DATE", "MATCHUP","AVAILABLE_FLAG"])

fullSeason = fullSeason.drop_duplicates(["GAME_ID"])

# Filter to 2020 - 2024

recentSeasons = fullSeason[fullSeason["SEASON_YEAR"] >= "2020-21"]


print(len(recentSeasons))

