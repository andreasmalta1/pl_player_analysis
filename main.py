import os
import pandas as pd
import numpy as np
import time

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from categories.nationalities import nations
from categories.cards import get_cards_info, cards_combined
from utils import get_info, get_num_matches
from teams import TEAMS

pd.options.mode.chained_assignment = None

COLUMNS = [
    "Player",
    "Nation",
    "Pos",
    "Age",
    "MP",
    "Starts",
    "Min",
    "90s",
    "Gls",
    "Ast",
    "G+A",
    "G-PK",
    "PK",
    "PKatt",
    "CrdY",
    "CrdR",
    "xG",
    "npxG",
    "xAG",
    "npxG+xAG",
    "PrgC",
    "PrgP",
    "PrgR",
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
]

NINETY_COLUMNS = [
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
]

AGGREGATOR = {
    "Nation": "first",
    "Pos": "first",
    "Age": "first",
    "MP": "sum",
    "Starts": "sum",
    "Min": "sum",
    "90s": "sum",
    "Gls": "sum",
    "Ast": "sum",
    "G+A": "sum",
    "G-PK": "sum",
    "PK": "sum",
    "PKatt": "sum",
    "CrdY": "sum",
    "CrdR": "sum",
    "xG": "sum",
    "npxG": "sum",
    "xAG": "sum",
    "npxG+xAG": "sum",
    "PrgC": "sum",
    "PrgP": "sum",
    "PrgR": "sum",
    "club_name": "first",
    "club_id": "first",
}


def get_all_data():
    league_url = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
    comps_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
    league_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/c9/misc/{team_name}-Match-Logs-Premier-League"
    comps_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    leagues = ["epl", "laliga", "ligue1", "bundesliga", "seriea"]
    for league in leagues:
        if not os.path.isdir(f"csvs/{league}"):
            os.makedirs(f"csvs/{league}")

    list_leagues_all, list_comps_all = [], []

    for league in TEAMS:
        list_league_combined, list_comps_combined = [], []
        for team_name in TEAMS[league]:
            print(team_name)
            time.sleep(5)
            fbref_id = TEAMS[league][team_name]["fbref_id"]
            fotmob_id = TEAMS[league][team_name]["fotmob_id"]
            if TEAMS[league][team_name].get("short_name"):
                team_name = TEAMS[league][team_name].get("short_name")

            df_league = get_info(
                league_url.format(fbref_id=fbref_id, team_name=team_name)
            )
            df_comps = get_info(
                comps_url.format(fbref_id=fbref_id, team_name=team_name)
            )
            df_league.drop(columns=df_league.columns[-1], axis=1, inplace=True)
            df_comps.drop(columns=df_comps.columns[-1], axis=1, inplace=True)
            df_league.columns = COLUMNS
            df_comps.columns = COLUMNS
            df_league = df_league[df_league.MP != "0"]
            df_comps = df_comps[df_comps.MP != "0"]
            df_league = df_league[df_league["90s"] != "0.0"]
            df_comps = df_comps[df_comps["90s"] != "0.0"]
            df_league = df_league.dropna().reset_index(drop=True)
            df_comps = df_comps.dropna().reset_index(drop=True)

            df_comps = df_comps.astype(
                {
                    "MP": "int",
                    "Starts": "int",
                    "Min": "int",
                    "90s": "float",
                    "Gls": "int",
                    "Ast": "int",
                    "G+A": "int",
                    "G-PK": "int",
                    "PK": "int",
                    "PKatt": "int",
                    "CrdY": "int",
                    "CrdR": "int",
                    "xG": "float",
                    "npxG": "float",
                    "xAG": "float",
                    "npxG+xAG": "float",
                    "PrgC": "int",
                    "PrgP": "int",
                    "PrgR": "int",
                }
            )

            df_league["club_name"] = team_name
            df_comps["club_name"] = team_name
            df_league["club_id"] = fotmob_id
            df_comps["club_id"] = fotmob_id

            df_league_matches = get_info(
                league_games_url.format(fbref_id=fbref_id, team_name=team_name)
            )
            df_comps_matches = get_info(
                comps_games_url.format(fbref_id=fbref_id, team_name=team_name)
            )

            file_path = f"csvs/{league}/{team_name.lower()}"
            if not os.path.isdir(file_path):
                os.makedirs(file_path)

            df_league.to_csv(os.path.join(file_path, "league_info.csv"))
            df_comps.to_csv(os.path.join(file_path, "comps_info.csv"))
            df_league_matches.to_csv(os.path.join(file_path, "league_matches.csv"))
            df_comps_matches.to_csv(os.path.join(file_path, "comps_matches.csv"))

            df_league.drop(NINETY_COLUMNS, axis=1)
            df_comps.drop(NINETY_COLUMNS, axis=1)
            list_league_combined.append(df_league)
            list_comps_combined.append(df_comps)

        file_path = f"csvs/{league}"

        df_league_combined = pd.concat(list_league_combined, axis=0, ignore_index=True)
        df_comps_combined = pd.concat(list_comps_combined, axis=0, ignore_index=True)

        df_league_combined.to_csv(os.path.join(file_path, "all_league_info.csv"))
        df_comps_combined.to_csv(os.path.join(file_path, "all_comps_info.csv"))

        duplicate_rows = df_comps_combined[df_comps_combined.duplicated(["Player"])]
        df_comps_combined.drop_duplicates(subset=["Player"], inplace=True)
        df_comps_combined = (
            pd.concat([df_comps_combined, duplicate_rows])
            .groupby(["Player"], as_index=False)
            .agg(AGGREGATOR)
        )

        for i in df_comps_combined.index:
            df_comps_combined.at[i, "Gls90"] = int(
                df_comps_combined.at[i, "Gls"]
            ) / float(df_comps_combined.at[i, "90s"])

        df_comps_combined.round(decimals=2)
        # df_league_combined.to_csv(os.path.join(file_path, "all_league_info2.csv"))
        df_comps_combined.to_csv(os.path.join(file_path, "all_comps_info3.csv"))


def main():
    get_all_data()

    # df = pd.read_csv("csvs/epl/all_comps_info.csv")
    # duplicateRows = df[df.duplicated(["Player"])]
    # df.drop_duplicates(subset=["Player"], inplace=True)

    # out = (
    #     pd.concat([df, duplicateRows])
    #     .groupby(["Player"], as_index=False)
    #     .agg(aggregator)
    # )
    # print(out)

    # out.to_csv("test2.csv")

    # print(df.columns)
    # 10-6
    # 17-16
    # 762 players

    return

    for competition in ["pl", "comps"]:
        for category in [
            "gls",
            "ast",
            "g+a",
            "gls90",
            "ast90",
            "g+a90",
            "minutes",
            "cards",
        ]:
            if not os.path.isdir(f"figures/{category}/{competition}"):
                os.makedirs(f"figures/{category}/{competition}")

    if not os.path.isdir("figures/nationalities"):
        os.makedirs("figures/nationalities")

    (
        pl_goal_list,
        comps_goal_list,
        pl_goal90_list,
        comps_goal90_list,
        pl_minutes_list,
        comps_minutes_list,
        pl_cards_list,
        comps_cards_list,
    ) = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )

    for team_name in TEAMS:
        fbref_id = TEAMS[team_name]["fbref_id"]
        fotmob_id = TEAMS[team_name]["fotmob_id"]

        df_pl = get_info(pl_url.format(fbref_id=fbref_id, team_name=team_name))
        df_comps = get_info(comps_url.format(fbref_id=fbref_id, team_name=team_name))
        matches_pl = get_num_matches(
            pl_games_url.format(fbref_id=fbref_id, team_name=team_name)
        )
        matches_comp = get_num_matches(
            comps_games_url.format(fbref_id=fbref_id, team_name=team_name)
        )

        if TEAMS[team_name].get("short_name"):
            team_name = TEAMS[team_name].get("short_name")

        (
            df_pl_goals_total,
            df_pl_goals_90,
            df_comps_goal_total,
            df_comps_goal_90,
        ) = goals_and_assists(df_pl, df_comps, team_name, fotmob_id)
        df_pl_minutes, df_comps_minutes = minutes(
            df_pl, df_comps, team_name, matches_pl, matches_comp, fotmob_id
        )
        df_pl_cards, df_comps_cards = get_cards_info(df_pl, df_comps)

        pl_goal_list.append(df_pl_goals_total)
        comps_goal_list.append(df_comps_goal_total)
        pl_goal90_list.append(df_pl_goals_90)
        comps_goal90_list.append(df_comps_goal_90)
        pl_minutes_list.append(df_pl_minutes)
        comps_minutes_list.append(df_comps_minutes)
        pl_cards_list.append(df_pl_cards)
        comps_cards_list.append(df_comps_cards)

    df_goals_pl = pd.concat(pl_goal_list, axis=0, ignore_index=True)
    df_goals_comps = pd.concat(comps_goal_list, axis=0, ignore_index=True)
    df_goals_90_pl = pd.concat(pl_goal90_list, axis=0, ignore_index=True)
    df_goals_90_comps = pd.concat(comps_goal90_list, axis=0, ignore_index=True)
    df_minutes_pl = pd.concat(pl_minutes_list, axis=0, ignore_index=True)
    df_minutes_comps = pd.concat(comps_minutes_list, axis=0, ignore_index=True)
    df_pl_cards = pd.concat(pl_cards_list, axis=0, ignore_index=True)
    df_comps_cards = pd.concat(comps_cards_list, axis=0, ignore_index=True)

    goals_and_assists_combined(
        df_goals_pl, df_goals_comps, df_goals_90_pl, df_goals_90_comps
    )
    minutes_combined(df_minutes_pl, df_minutes_comps)
    nations()
    cards_combined(df_pl_cards, df_comps_cards)


if __name__ == "__main__":
    main()

# TODO
# Get fbref & fotmob info from all 5 leagues
# When saving csvs, save a combined for each league and a combined for all top 5 leagues
# Merge players with the same name (same fbref id)
# Add nationalities csvs
# Clean up code
# Add club name
# Works, now when saving combined, we need to delete per 90 and the work it out for all players for all columns.
# Create small functions to remove double works for cleaning
