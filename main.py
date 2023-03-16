import os
import pandas as pd

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from categories.nationalities import nations
from categories.cards import get_cards_info, cards_combined
from utils import get_info, get_num_matches
from teams import TEAMS

pd.options.mode.chained_assignment = None


def get_all_data():
    league_url = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
    comps_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
    league_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/c9/misc/{team_name}-Match-Logs-Premier-League"
    comps_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    leagues = ["epl", "laliga", "ligue1", "bundesliga", "seriea"]
    for league in leagues:
        if not os.path.isdir(f"csvs/{league}"):
            os.makedirs(f"csvs/{league}")

    for league in TEAMS:
        for team_name in TEAMS[league]:
            fbref_id = TEAMS[league][team_name]["fbref_id"]
            if TEAMS[league][team_name].get("short_name"):
                team_name = TEAMS[league][team_name].get("short_name")

            df_league = get_info(
                league_url.format(fbref_id=fbref_id, team_name=team_name)
            )
            df_comps = get_info(
                comps_url.format(fbref_id=fbref_id, team_name=team_name)
            )
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


def main():
    get_all_data()
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
# Get fbref & fotmob info from all 5 teams
# When saving csvs, save a combined for each league and a combined for all top 5 leagues
# Add nationalities csvs
# Clean up code
