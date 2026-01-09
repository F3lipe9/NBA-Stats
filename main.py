import pandas as pd

# Gets User Inputs
yearWanted = str(input("What Year Do You Want To Look Into? "))
stat = str(input("What Stat Do You want? "))

# Create Data and Merge to create one DataFrame

playoffs = pd.read_csv("data/play_off_totals_2010_2024.csv")

regularSeason = pd.read_csv("data/regular_season_totals_2010_2024.csv")

fullSeason = pd.concat([regularSeason, playoffs])

# Clean Data

# Drop Unwanted Cols
fullSeason = fullSeason.drop(columns=["GP_RANK" ,"W_RANK","L_RANK","W_PCT_RANK","MIN_RANK","FGM_RANK",
                                      "FGA_RANK","FG_PCT_RANK","FG3M_RANK","FG3A_RANK","FG3_PCT_RANK",
                                      "FTM_RANK","FTA_RANK", "FT_PCT_RANK","OREB_RANK","DREB_RANK",
                                      "REB_RANK","AST_RANK","TOV_RANK","STL_RANK","BLK_RANK",
                                      "BLKA_RANK","PF_RANK","PFD_RANK","PTS_RANK","PLUS_MINUS_RANK",
                                        "TEAM_ID", "GAME_DATE", "MATCHUP","AVAILABLE_FLAG"])


# Filter to 2020 - 2024

recentSeasons = fullSeason[fullSeason["SEASON_YEAR"] >= "2020-21"]


# Check Validity
# From 2020-21 to 2023-24 there was approxamitly 5114 games
# 5114 * 2  = 10228, each game gets stat for each team
# My Data Set has 10238

# Map stat names to column names
statMapping = {
    "Points": "PTS",
    "3PM": "FG3M",
    "3PA": "FG3A",
    "FGM": "FGM",
    "FGA": "FGA",
    "FTM": "FTM",
    "FTA": "FTA",
    "Assists": "AST",
    "Rebounds": "REB",
    "OREB": "OREB",
    "DREB": "DREB",
    "Steals": "STL",
    "Blocks": "BLK",
    "Turnovers": "TOV",
    "Fouls": "PF",
    "Plus/Minus": "PLUS_MINUS"
}

# Get Stats Wanted
def getStat(yearWanted, stat):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    
    if stat == "Games":
        print(singleSeason.groupby(["TEAM_ABBREVIATION"]).size())
    elif stat in statMapping:
        columnName = statMapping[stat]
        print(singleSeason.groupby(["TEAM_ABBREVIATION"])[columnName].sum())
    else:
        print("Invalid stat. Please try again.")

# Run the function
getStat(yearWanted, stat)

