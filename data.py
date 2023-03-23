import os
import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

from constants import COLUMNS, NINETY_COLUMNS, TYPES_DICT, LEAGUES, COUNTRIES
from utils import get_info, drop_rows, remove_duplicates
from teams import TEAMS

LGE_URL = "https://fbref.com/en/squads/{fbref_id}/{team_name}-Stats"
COMPS_URL = "https://fbref.com/en/squads/{fbref_id}/2022-2023/all_comps/{team_name}-Stats-All-Competitions"
LGE_GAMES_URL = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/{lge_code}/misc/{team_name}-Match-Logs"
COMPS_GAMES_URL = "https://fbref.com/en/squads/{fbref_id}/2022-2023/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"
NATIONALITIES_URL = (
    "https://fbref.com/en/comps/{lge_code}/nations/{lge_name}-Nationalities"
)
GOALS_URL = "https://fbref.com/en/comps/{lge_code}/shooting/{lge_name}-Stats"


def get_goals(url):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = uc.Chrome(chrome_options=chrome_options)

    driver.get(url)

    source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(source, "lxml")

    rows = soup.find("table", id="stats_shooting").find("tbody").find_all("tr")

    df_goals = pd.DataFrame(columns=["Nation", "Goals"])
    nation = []
    goals = []

    for row in rows:
        cells = row.find_all("td")
        if cells:
            nation.append(cells[1].get_text())
            goals.append(cells[7].get_text())

    for i in range(len(goals)):
        df_goals.loc[i] = [nation[i], int(goals[i])]

    return df_goals


def get_teams_data():
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

            df_lge = get_info(LGE_URL.format(fbref_id=fbref_id, team_name=team_name))
            df_comps = get_info(
                COMPS_URL.format(fbref_id=fbref_id, team_name=team_name)
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
                LGE_GAMES_URL.format(
                    fbref_id=fbref_id, lge_code=lge_code, team_name=team_name
                )
            )
            df_comps_mth = get_info(
                COMPS_GAMES_URL.format(fbref_id=fbref_id, team_name=team_name)
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


def get_nationalities_data():
    df_total_times = pd.DataFrame(columns=["Nation", "Min"])
    df_total_players = pd.DataFrame(columns=["Nation", "# Players"])
    df_total_goals = pd.DataFrame(columns=["Nation", "Goals"])

    for lge in LEAGUES:
        lge_name = LEAGUES[lge]["lge_name"].replace(" ", "-")
        lge_code = LEAGUES[lge]["lge_code"][1:]

        html = pd.read_html(
            NATIONALITIES_URL.format(lge_code=lge_code, lge_name=lge_name), header=0
        )
        df = html[0]
        df = df.drop(["Rk", "List"], axis=1)
        df = df.dropna()
        df = drop_rows(df, "# Players", "# Players")
        df = df.astype({"# Players": "int", "Min": "int"})
        # print(df["Nation"])
        df2 = df
        df["Nation"] = [x.split(" ")[0].lower() for x in df["Nation"]]
        print(df["Nation"])
        df2["Nation"] = df2["Nation"].str.split(" ", 1)
        print(df2["Nation"])

        df_players = df.sort_values(by=["# Players"])
        df_players = df_players.drop(["Min"], axis=1)
        if lge != "ucl" and lge != "uel":
            df_total_players = pd.concat(
                [df_total_players, df_players], ignore_index=True
            )

        df_players = df_players.tail(10)

        df_times = df
        df_times = df_times.sort_values(by=["Min"])
        df_times = df_times.drop(["# Players"], axis=1)
        if lge != "ucl" and lge != "uel":
            df_total_times = pd.concat([df_total_times, df_times], ignore_index=True)

        df_times = df_times.tail(10)

        df_goals = get_goals(GOALS_URL.format(lge_code=lge_code, lge_name=lge_name))

        if lge != "ucl" and lge != "uel":
            df_total_goals = pd.concat([df_total_goals, df_goals], ignore_index=True)

        df_sum = df_goals.groupby("Nation")["Goals"].sum().reset_index()
        df_sum = df_sum.sort_values(by=["Goals"])
        df_sum = df_sum.tail(10)

        for i, row in df_sum.iterrows():
            country = COUNTRIES.get(df_sum.at[i, "Nation"])
            if country:
                df_sum.at[i, "Nation"] = country

        file_path = f"csvs/{lge}"
        df_players.to_csv(os.path.join(file_path, "league_players.csv"))
        df_times.to_csv(os.path.join(file_path, "league_times.csv"))
        df_sum.to_csv(os.path.join(file_path, "league_goals.csv"))

    df_total_players = df_total_players.groupby("Nation", as_index=False).sum()
    df_total_players = df_total_players.sort_values(by=["# Players"])
    df_total_players = df_total_players.tail(10)

    df_total_times = df_total_times.groupby("Nation", as_index=False).sum()
    df_total_times = df_total_times.sort_values(by=["Min"])
    df_total_times = df_total_times.tail(10)

    df_total_goals = df_total_goals.groupby("Nation", as_index=False).sum()
    df_total_goals = df_total_goals.sort_values(by=["Goals"])
    df_total_goals = df_total_goals.tail(10)

    for i, row in df_total_goals.iterrows():
        country = COUNTRIES.get(df_total_goals.at[i, "Nation"])
        if country:
            df_total_goals.at[i, "Nation"] = country

    file_path = "csvs"
    df_total_players.to_csv(os.path.join(file_path, "combined_total_players.csv"))
    df_total_times.to_csv(os.path.join(file_path, "combined_total_times.csv"))
    df_total_goals.to_csv(os.path.join(file_path, "combined_total_goals.csv"))


def get_data():
    for lge in LEAGUES:
        if not os.path.isdir(f"csvs/{lge}"):
            os.makedirs(f"csvs/{lge}")

    # get_teams_data()
    get_nationalities_data()
