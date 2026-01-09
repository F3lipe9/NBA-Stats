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

# Get Stats Wanted

def points(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["PTS"].sum())

def threePtsMade(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FG3M"].sum())

def threePtsAttempted(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FG3A"].sum())

def fieldGoalsMade(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FGM"].sum())

def fieldGoalsAttempted(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FGA"].sum())

def freeThrowsMade(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FTM"].sum())

def freeThrowsAttempted(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["FTA"].sum())

def assists(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["AST"].sum())

def rebounds(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["REB"].sum())

def offensiveRebounds(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["OREB"].sum())

def defensiveRebounds(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["DREB"].sum())

def steals(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["STL"].sum())

def blocks(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["BLK"].sum())

def turnovers(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["TOV"].sum())

def personalFouls(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["PF"].sum())

def plusMinus(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"])["PLUS_MINUS"].sum())

def games(yearWanted):
    singleSeason = recentSeasons[recentSeasons["SEASON_YEAR"] == yearWanted]
    print(singleSeason.groupby(["TEAM_ABBREVIATION"]).size())

# Switch Case To Run Function of Stat Wanted
match stat:
    case "Points":
        points(yearWanted)
    case "3PM":
        threePtsMade(yearWanted)
    case "3PA":
        threePtsAttempted(yearWanted)
    case "FGM":
        fieldGoalsMade(yearWanted)
    case "FGA":
        fieldGoalsAttempted(yearWanted)
    case "FTM":
        freeThrowsMade(yearWanted)
    case "FTA":
        freeThrowsAttempted(yearWanted)
    case "Assists":
        assists(yearWanted)
    case "Rebounds":
        rebounds(yearWanted)
    case "OREB":
        offensiveRebounds(yearWanted)
    case "DREB":
        defensiveRebounds(yearWanted)
    case "Steals":
        steals(yearWanted)
    case "Blocks":
        blocks(yearWanted)
    case "Turnovers":
        turnovers(yearWanted)
    case "Fouls":
        personalFouls(yearWanted)
    case "Plus/Minus":
        plusMinus(yearWanted)
    case "Games":
        games(yearWanted)
    case _:
        print("Invalid stat. Please try again.")

