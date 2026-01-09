# NBA-Stats

A Python-based NBA statistics analyzer that aggregates and displays team performance data from the 2020-21 to 2023-24 seasons, combining both regular season and playoff statistics.

## Description

This project processes NBA team totals data from CSV files, allowing users to query specific statistics for any team across different seasons. The tool merges regular season and playoff data to provide comprehensive team performance insights.

## Features

- **Combined Data Analysis**: Merges regular season and playoff statistics into a unified dataset
- **Season Filtering**: Focuses on recent seasons (2020-21 onwards)
- **Multiple Statistics**: Query various team statistics including:
  - Points
  - Field Goals (Made/Attempted)
  - 3-Pointers (Made/Attempted)
  - Free Throws (Made/Attempted)
  - Assists
  - Rebounds (Total/Offensive/Defensive)
  - Steals
  - Blocks
  - Turnovers
  - Personal Fouls
  - Plus/Minus
  - Games Played

## Requirements

- Python 3.10+
- pandas

## Installation

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Usage

Run the script:
```bash
python main.py
```

You'll be prompted to enter:
1. **Season Year**: Enter in format `YYYY-YY` (e.g., `2023-24`)
2. **Statistic**: Choose from available stats (e.g., `Points`, `Assists`, `3PM`, etc.)

### Available Statistics

- `Points` - Total points scored
- `3PM` - Three-pointers made
- `3PA` - Three-pointers attempted
- `FGM` - Field goals made
- `FGA` - Field goals attempted
- `FTM` - Free throws made
- `FTA` - Free throws attempted
- `Assists` - Total assists
- `Rebounds` - Total rebounds
- `OREB` - Offensive rebounds
- `DREB` - Defensive rebounds
- `Steals` - Total steals
- `Blocks` - Total blocks
- `Turnovers` - Total turnovers
- `Fouls` - Personal fouls
- `Plus/Minus` - Plus/minus rating
- `Games` - Games played

## Data Files

The project requires two CSV files in the `data/` directory:
- `play_off_totals_2010_2024.csv`
- `regular_season_totals_2010_2024.csv`

## How It Works

1. Loads regular season and playoff data from CSV files
2. Concatenates both datasets
3. Removes duplicate games and unnecessary ranking columns
4. Filters data to seasons from 2020-21 onwards
5. Groups statistics by team abbreviation
6. Displays aggregated results for the requested statistic

## Example

```
What Year Do You Want To Look Into? 2023-24
What Stat Do You want? Points

TEAM_ABBREVIATION
ATL     8910
BOS     9350
BKN     8654
...
```

## Data Validation

The dataset contains approximately 10,238 team records from 2020-21 to 2023-24 seasons (with each game counted once per team).

## License

This project is for educational and personal use.