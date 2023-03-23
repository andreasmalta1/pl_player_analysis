import os
import pandas as pd

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from categories.nationalities import nations
from categories.cards import cards_combined
from utils import get_info, drop_rows, remove_duplicates
from constants import COLUMNS, NINETY_COLUMNS, TYPES_DICT, LEAGUES, CATEGORIES
from teams import TEAMS

pd.options.mode.chained_assignment = None


def get_all_data():
    lge_url = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
    comps_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
    lge_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/{lge_code}/misc/{team_name}-Match-Logs"
    comps_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    for lge in LEAGUES:
        if not os.path.isdir(f"csvs/{lge}"):
            os.makedirs(f"csvs/{lge}")

    list_lges_all, list_comps_all = [], []

    for lge in TEAMS:
        list_lge_combined, list_comps_combined = [], []
        lge_code = LEAGUES[lge]["lge_code"]

        for team_name in TEAMS[lge]:
            print(team_name)
            fbref_id = TEAMS[lge][team_name]["fbref_id"]
            fotmob_id = TEAMS[lge][team_name]["fotmob_id"]
            if TEAMS[lge][team_name].get("short_name"):
                team_name = TEAMS[lge][team_name].get("short_name")

            df_lge = get_info(lge_url.format(fbref_id=fbref_id, team_name=team_name))
            df_comps = get_info(
                comps_url.format(fbref_id=fbref_id, team_name=team_name)
            )
            df_lge.drop(columns=df_lge.columns[-1], axis=1, inplace=True)
            df_comps.drop(columns=df_comps.columns[-1], axis=1, inplace=True)
            df_lge.columns = COLUMNS
            df_comps.columns = COLUMNS

            df_lge = drop_rows(df_lge, "MP", "0")
            df_lge = drop_rows(df_lge, "90s", "0.0")
            df_comps = drop_rows(df_comps, "MP", "0")
            df_comps = drop_rows(df_comps, "90s", "0.0")

            df_lge = df_lge.dropna().reset_index(drop=True)
            df_comps = df_comps.dropna().reset_index(drop=True)

            df_lge = df_lge.astype(TYPES_DICT)
            df_comps = df_comps.astype(TYPES_DICT)

            df_lge["club_name"] = team_name
            df_comps["club_name"] = team_name

            df_lge["club_id"] = fotmob_id
            df_comps["club_id"] = fotmob_id

            df_lge["lge"] = lge
            df_comps["lge"] = lge

            df_lge = df_lge.replace("gf GUF", "fr FRA")
            df_comps = df_comps.replace("gf GUF", "fr FRA")

            for i in df_lge.index:
                df_lge.at[i, "G+A"] = int(df_lge.at[i, "Gls"]) + int(
                    df_lge.at[i, "Ast"]
                )

            for i in df_comps.index:
                df_comps.at[i, "G+A"] = int(df_comps.at[i, "Gls"]) + int(
                    df_comps.at[i, "Ast"]
                )

            df_lge_mth = get_info(
                lge_games_url.format(
                    fbref_id=fbref_id, lge_code=lge_code, team_name=team_name
                )
            )
            df_comps_mth = get_info(
                comps_games_url.format(fbref_id=fbref_id, team_name=team_name)
            )

            file_path = f"csvs/{lge}/{team_name.lower()}"
            if not os.path.isdir(file_path):
                os.makedirs(file_path)

            df_lge.to_csv(os.path.join(file_path, "league_info.csv"))
            df_comps.to_csv(os.path.join(file_path, "comps_info.csv"))
            df_lge_mth.to_csv(os.path.join(file_path, "league_matches.csv"))
            df_comps_mth.to_csv(os.path.join(file_path, "comps_matches.csv"))

            df_lge.drop(NINETY_COLUMNS, axis=1)
            df_comps.drop(NINETY_COLUMNS, axis=1)
            list_lge_combined.append(df_lge)
            list_comps_combined.append(df_comps)

        file_path = f"csvs/{lge}"

        df_lge_combined = pd.concat(list_lge_combined, axis=0, ignore_index=True)
        df_comps_combined = pd.concat(list_comps_combined, axis=0, ignore_index=True)

        df_lge_combined = remove_duplicates(df_lge_combined)
        df_comps_combined = remove_duplicates(df_comps_combined)

        df_lge_combined.to_csv(os.path.join(file_path, "all_league_info.csv"))
        df_comps_combined.to_csv(os.path.join(file_path, "all_comps_info.csv"))

        list_lges_all.append(df_lge_combined)
        list_comps_all.append(df_comps_combined)

    file_path = f"csvs"
    df_lge_all = pd.concat(list_lges_all, axis=0, ignore_index=True)
    df_comps_all = pd.concat(list_comps_all, axis=0, ignore_index=True)

    df_lge_all = remove_duplicates(df_lge_all)
    df_comps_all = remove_duplicates(df_comps_all)

    df_lge_all.to_csv(os.path.join(file_path, "all_leagues_info.csv"))
    df_comps_all.to_csv(os.path.join(file_path, "all_comps_info.csv"))


def main():
    get_all_data()

    for lge in LEAGUES:
        for competition in [lge, "comps"]:
            for category in CATEGORIES:
                if not os.path.isdir(f"figures/{lge}/{category}/{competition}"):
                    os.makedirs(f"figures/{lge}/{category}/{competition}")

    for category in CATEGORIES:
        if not os.path.isdir(f"figures/combined/{category}"):
            os.makedirs(f"figures/combined/{category}")

    if not os.path.isdir("figures/nationalities"):
        os.makedirs("figures/nationalities")

    for lge in TEAMS:
        for team_name in TEAMS[lge]:
            print(team_name)
            fotmob_id = TEAMS[lge][team_name]["fotmob_id"]
            if TEAMS[lge][team_name].get("short_name"):
                team_name = TEAMS[lge][team_name].get("short_name")

            df_lge = pd.read_csv(f"csvs/{lge}/{team_name}/league_info.csv")
            df_comps = pd.read_csv(f"csvs/{lge}/{team_name}/comps_info.csv")
            df_lge_mth = pd.read_csv(f"csvs/{lge}/{team_name}/league_matches.csv")
            df_comps_mth = pd.read_csv(f"csvs/{lge}/{team_name}/comps_matches.csv")

            goals_and_assists(df_lge, df_comps, team_name, fotmob_id, lge)
            minutes(
                df_lge, df_comps, df_lge_mth, df_comps_mth, team_name, fotmob_id, lge
            )

            df_lge = pd.read_csv(f"csvs/{lge}/all_league_info.csv")
            df_comps = pd.read_csv(f"csvs/{lge}/all_comps_info.csv")

        goals_and_assists_combined(df_lge, df_comps, lge)
        minutes_combined(df_lge, df_comps, lge)
        cards_combined(df_lge, df_comps, lge)

    df_lge = pd.read_csv(f"csvs/all_leagues_info.csv")
    df_comps = pd.read_csv(f"csvs/all_comps_info.csv")

    goals_and_assists_combined(df_lge, df_comps, None)
    minutes_combined(df_lge, df_comps, None)
    cards_combined(df_lge, df_comps, None)

    # nations()


if __name__ == "__main__":
    main()

# TODO
# Work out the additions myself
# 4. Get nationalities csvs
# 5. Clean up code and refactor
# 6. Add plot types
