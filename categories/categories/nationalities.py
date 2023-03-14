import pandas as pd
import warnings
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from plots.plots_nationalties import plt_nationalities, plt_nationalities_combined
from utils import dict_conversion

warnings.filterwarnings("ignore")


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


def nations():
    leagues = {
        "epl": {
            "title": "Premier League",
            "nations_url": "https://fbref.com/en/comps/9/nations/Premier-League-Nationalities",
            "goals_url": "https://fbref.com/en/comps/9/shooting/Premier-League-Stats",
            "fotmob_id": 47,
        },
        "laliga": {
            "title": "La Liga",
            "nations_url": "https://fbref.com/en/comps/12/nations/La-Liga-Nationalities",
            "goals_url": "https://fbref.com/en/comps/12/shooting/La-Liga-Stats",
            "fotmob_id": 87,
        },
        "bundesliga": {
            "title": "Bundesliga",
            "nations_url": "https://fbref.com/en/comps/20/nations/Bundesliga-Nationalities",
            "goals_url": "https://fbref.com/en/comps/20/shooting/Bundesliga-Stats",
            "fotmob_id": 54,
        },
        "seriea": {
            "title": "Serie A",
            "nations_url": "https://fbref.com/en/comps/11/nations/Serie-A-Nationalities",
            "goals_url": "https://fbref.com/en/comps/11/shooting/Serie-A-Stats",
            "fotmob_id": 55,
        },
        "ligue1": {
            "title": "Ligue 1",
            "nations_url": "https://fbref.com/en/comps/13/nations/Ligue-1-Nationalities",
            "goals_url": "https://fbref.com/en/comps/13/shooting/Ligue-1-Stats",
            "fotmob_id": 53,
        },
        "ucl": {
            "title": "Uefa Champions League",
            "nations_url": "https://fbref.com/en/comps/8/nations/Champions-League-Nationalities",
            "goals_url": "https://fbref.com/en/comps/8/shooting/Champions-League-Stats",
            "fotmob_id": 42,
        },
        # "uel": {
        #     "title": "Uefa Europe Lague",
        #     "nations_url": "https://fbref.com/en/comps/19/2022/nations/2022-Nationalities",
        #     "goals_url": "https://fbref.com/en/comps/19/shooting/Europa-League-Stats",
        #     "fotmob_id": 73,
        # },
    }

    df_total_times = pd.DataFrame(columns=["Nation", "Min"])
    df_total_players = pd.DataFrame(columns=["Nation", "# Players"])
    df_total_goals = pd.DataFrame(columns=["Nation", "Goals"])
    df = pd.DataFrame()

    for competition in leagues:
        comp_title = leagues[competition]["title"]
        nations_url = leagues[competition]["nations_url"]
        goals_url = leagues[competition]["goals_url"]
        fotmob_id = leagues[competition]["fotmob_id"]

        html = pd.read_html(nations_url, header=0)
        df = html[0]
        df = df.drop(["Rk", "List"], axis=1)
        df["Nation"] = df["Nation"].str.split(" ", 1)

        drop_rows = []

        for index, row in df.iterrows():
            row["Nation"] = row["Nation"].pop()
            if row["# Players"] == "# Players":
                drop_rows.append(index)

        df = df.drop(labels=drop_rows)

        df["# Players"] = df["# Players"].astype(float)
        df["Min"] = df["Min"].astype(float)

        df_players = df.sort_values(by=["# Players"])
        df_players = df_players.drop(["Min"], axis=1)
        if competition != "ucl" and competition != "uel":
            df_total_players = pd.concat(
                [df_total_players, df_players], ignore_index=True
            )

        df_players = df_players.tail(10)

        df_times = df
        df_times = df_times.dropna()
        df_times = df_times.sort_values(by=["Min"])
        df_times = df_times.drop(["# Players"], axis=1)
        if competition != "ucl" and competition != "uel":
            df_total_times = pd.concat([df_total_times, df_times], ignore_index=True)

        df_times = df_times.tail(10)
        df = get_goals(goals_url)

        if competition != "ucl" and competition != "uel":
            df_total_goals = pd.concat([df_total_goals, df], ignore_index=True)

        df_sum = df.groupby("Nation")["Goals"].sum().reset_index()
        df_sum = df_sum.sort_values(by=["Goals"])
        df_sum = df_sum.tail(10)

        for i, row in df_sum.iterrows():
            country = dict_conversion(df_sum.at[i, "Nation"])
            if country:
                df_sum.at[i, "Nation"] = country

        plt_nationalities(
            df_players, df_times, df_sum, competition, comp_title, fotmob_id
        )

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
        country = dict_conversion(df_total_goals.at[i, "Nation"])
        if country:
            df_total_goals.at[i, "Nation"] = country

    plt_nationalities_combined(df_total_players, df_total_times, df_total_goals)