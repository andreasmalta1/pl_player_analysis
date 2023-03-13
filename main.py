import os
import pandas as pd

from categories.goals_assists import goals_and_assists, goals_and_assists_combined
from categories.minutes_played import minutes, minutes_combined
from utils import get_info, get_num_matches
from teams import TEAMS

pd.options.mode.chained_assignment = None


def nations():
    # pl_url = "https://fbref.com/en/comps/9/nations/Premier-League-Nationalities"
    # liga_url = "https://fbref.com/en/comps/12/nations/La-Liga-Nationalities"
    # bundesliga_url = "https://fbref.com/en/comps/20/nations/Bundesliga-Nationalities"
    # italy_url = "https://fbref.com/en/comps/11/nations/Serie-A-Nationalities"
    # french_url = "https://fbref.com/en/comps/13/nations/Ligue-1-Nationalities"
    # cl_url = "https://fbref.com/en/comps/8/nations/Champions-League-Nationalities"
    # # uel_url = "https://fbref.com/en/comps/19/2022/nations/2022-Nationalities"

    # league_urls = {
    #     "epl": {"url": pl_url, "color": "mediumpurple"},
    #     "laliga": {"url": liga_url, "color": "salmon"},
    #     "bundesliga": {"url": bundesliga_url, "color": "lightcoral"},
    #     "seriea": {"url": italy_url, "color": "lightcyan"},
    #     "ligue1": {"url": french_url, "color": "lemonchiffon"},
    #     "ucl": {"url": cl_url, "color": "cornflowerblue"},
    #     # "uel": {"url": uel_url, "color": "orange"},
    # }

    # df_total_times = pd.DataFrame(columns=["Nation", "Min"])
    # df_total_players = pd.DataFrame(columns=["Nation", "# Players"])
    # df_total_goals = pd.DataFrame(columns=["Nation", "Goals"])
    # df = pd.DataFrame()

    # for competition in league_urls:
    #     url = league_urls[competition]["url"]
    #     color = league_urls[competition]["color"]

    #     if competition == "epl":
    #         comp_title = "Premier League"
    #         goals_url = "https://fbref.com/en/comps/9/shooting/Premier-League-Stats"
    #     if competition == "laliga":
    #         comp_title = "La Liga"
    #         goals_url = "https://fbref.com/en/comps/12/shooting/La-Liga-Stats"
    #     if competition == "bundesliga":
    #         comp_title = "Bundesliga"
    #         goals_url = "https://fbref.com/en/comps/20/shooting/Bundesliga-Stats"
    #     if competition == "seriea":
    #         comp_title = "Serie A"
    #         goals_url = "https://fbref.com/en/comps/11/shooting/Serie-A-Stats"
    #     if competition == "ligue1":
    #         comp_title = "Ligue 1"
    #         goals_url = "https://fbref.com/en/comps/13/shooting/Ligue-1-Stats"
    #     if competition == "ucl":
    #         comp_title = "Uefa Champions League"
    #         goals_url = "https://fbref.com/en/comps/8/shooting/Champions-League-Stats"
    #     if competition == "uel":
    #         comp_title = "Uefa Europa League"
    #         goals_url = "https://fbref.com/en/comps/19/2022/shooting/2022-Stats"

    #     html = pd.read_html(url, header=0)
    #     df = html[0]
    #     df = df.drop(["Rk", "List"], axis=1)
    #     df["Nation"] = df["Nation"].str.split(" ", 1)

    #     drop_rows = []

    #     for index, row in df.iterrows():
    #         row["Nation"] = row["Nation"].pop()
    #         if row["# Players"] == "# Players":
    #             drop_rows.append(index)

    #     df = df.drop(labels=drop_rows)

    #     df["# Players"] = df["# Players"].astype(float)
    #     df["Min"] = df["Min"].astype(float)

    #     df_players = df.sort_values(by=["# Players"])
    #     df_players = df_players.drop(["Min"], axis=1)
    #     if competition != "ucl" and competition != "uel":
    #         df_total_players = pd.concat(
    #             [df_total_players, df_players], ignore_index=True
    #         )

    #     df_players = df_players.tail(10)

    #     df_times = df
    #     df_times = df_times.dropna()
    #     df_times = df_times.sort_values(by=["Min"])
    #     df_times = df_times.drop(["# Players"], axis=1)
    #     if competition != "ucl" and competition != "uel":
    #         df_total_times = pd.concat([df_total_times, df_times], ignore_index=True)

    #     df_times = df_times.tail(10)
    pass


def main():
    pl_url = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
    comps_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
    pl_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/c9/misc/{team_name}-Match-Logs-Premier-League"
    comps_games_url = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    for competition in ["pl", "comps"]:
        for category in ["gls", "ast", "g+a", "minutes"]:
            if not os.path.isdir(f"figures/{category}/{competition}"):
                os.makedirs(f"figures/{category}/{competition}")

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
