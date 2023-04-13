import os
import pandas as pd

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from categories.cards import cards_combined
from categories.progression import progression, progression_combined
from categories.leagues_race import leagues_point_race
from plots.plots_nationalities import plt_nationalities, plt_nationalities_combined
from data import get_data

from constants import LEAGUES, CATEGORIES
from teams import TEAMS

pd.options.mode.chained_assignment = None


def main():
    # get_data()

    # for lge in LEAGUES:
    #     for competition in [lge, "comps"]:
    #         for category in CATEGORIES:
    #             if category == "nationalities":
    #                 if not os.path.isdir(f"figures/{lge}/{category}"):
    #                     os.makedirs(f"figures/{lge}/{category}")
    #             elif lge not in ["ucl", "uel"]:
    #                 if not os.path.isdir(f"figures/{lge}/{category}/{competition}"):
    #                     os.makedirs(f"figures/{lge}/{category}/{competition}")

    # for category in CATEGORIES:
    #     if not os.path.isdir(f"figures/combined/{category}"):
    #         os.makedirs(f"figures/combined/{category}")

    # for lge in TEAMS:
    #     for team_name in TEAMS[lge]:
    #         print(team_name)
    #         fotmob_id = TEAMS[lge][team_name]["fotmob_id"]
    #         if TEAMS[lge][team_name].get("short_name"):
    #             team_name = TEAMS[lge][team_name].get("short_name")

    #         df_lge = pd.read_csv(f"csvs/{lge}/{team_name}/league_info.csv")
    #         df_comps = pd.read_csv(f"csvs/{lge}/{team_name}/comps_info.csv")
    #         df_lge_mth = pd.read_csv(f"csvs/{lge}/{team_name}/league_matches.csv")
    #         df_comps_mth = pd.read_csv(f"csvs/{lge}/{team_name}/comps_matches.csv")

    #         goals_and_assists(df_lge, df_comps, team_name, fotmob_id, lge)
    #         minutes(
    #             df_lge, df_comps, df_lge_mth, df_comps_mth, team_name, fotmob_id, lge
    #         )
    #         progression(df_lge, df_comps, team_name, fotmob_id, lge)

    #     df_lge = pd.read_csv(f"csvs/{lge}/all_league_info.csv")
    #     df_comps = pd.read_csv(f"csvs/{lge}/all_comps_info.csv")

    #     goals_and_assists_combined(df_lge, df_comps, lge)
    #     minutes_combined(df_lge, df_comps, lge)
    #     cards_combined(df_lge, df_comps, lge)
    #     progression_combined(df_lge, df_comps, lge)

    # for lge in LEAGUES:
    #     df_players = pd.read_csv(f"csvs/{lge}/league_players.csv")
    #     df_times = pd.read_csv(f"csvs/{lge}/league_times.csv")
    #     df_goals = pd.read_csv(f"csvs/{lge}/league_goals.csv")

    #     plt_nationalities(df_players, df_times, df_goals, lge)

    # df_lge = pd.read_csv(f"csvs/all_leagues_info.csv")
    # df_comps = pd.read_csv(f"csvs/all_comps_info.csv")
    # df_players = pd.read_csv(f"csvs/combined_total_players.csv")
    # df_times = pd.read_csv(f"csvs/combined_total_times.csv")
    # df_goals = pd.read_csv(f"csvs/combined_total_goals.csv")

    # goals_and_assists_combined(df_lge, df_comps, None)
    # minutes_combined(df_lge, df_comps, None)
    # cards_combined(df_lge, df_comps, None)
    # progression_combined(df_lge, df_comps, None)
    # plt_nationalities_combined(df_players, df_times, df_goals)

    leagues_point_race()


if __name__ == "__main__":
    main()

# TODO
# Logo on text (Man Utd)
# Fix annotaion overlap for progression
# Change annotation between teams and leagues
# Fix too many players in combined data
# Reduce # of code lines especially when plotting -- too many functions that do the same thing
