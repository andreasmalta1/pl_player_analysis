import os
import pandas as pd

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from categories.nationalities import nations
from utils import get_info, get_num_matches
from teams import TEAMS

pd.options.mode.chained_assignment = None


def main():
    pl_url = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
    comps_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
    pl_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/c9/misc/{team_name}-Match-Logs-Premier-League"
    comps_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    for competition in ["pl", "comps"]:
        for category in ["gls", "ast", "g+a", "minutes"]:
            if not os.path.isdir(f"figures/{category}/{competition}"):
                os.makedirs(f"figures/{category}/{competition}")

    if not os.path.isdir("figures/nationalities"):
        os.makedirs("figures/nationalities")

    pl_goal_list = []
    comps_goal_list = []
    pl_minutes_list = []
    comps_minutes_list = []

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

        df_pl_goals, df_comps_goals = goals_and_assists(
            df_pl, df_comps, team_name, fotmob_id
        )
        df_pl_minutes, df_comps_minutes = minutes(
            df_pl, df_comps, team_name, matches_pl, matches_comp, fotmob_id
        )

        pl_goal_list.append(df_pl_goals)
        comps_goal_list.append(df_comps_goals)
        pl_minutes_list.append(df_pl_minutes)
        comps_minutes_list.append(df_comps_minutes)

    df_goals_pl = pd.concat(pl_goal_list, axis=0, ignore_index=True)
    df_goals_comps = pd.concat(comps_goal_list, axis=0, ignore_index=True)
    df_minutes_pl = pd.concat(pl_minutes_list, axis=0, ignore_index=True)
    df_minutes_comps = pd.concat(comps_minutes_list, axis=0, ignore_index=True)

    goals_and_assists_combined(df_goals_pl, df_goals_comps)
    minutes_combined(df_minutes_pl, df_minutes_comps)
    nations()


if __name__ == "__main__":
    main()
# TODO
# Check whether I can get goals without UC
# Check about UEL
# Add league logo
# Modify backgrounds
