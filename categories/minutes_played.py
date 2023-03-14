from plots.plots_minutes import plt_minutes, plt_minutes_all
from utils import get_info


def get_minutes(df):
    df = df[["Player", "Nation", "Pos", "Age", "Min", "MP", "Starts", "90s"]]
    df = df[~df["Min"].isna()]
    df = df[~df["Min"].isna()]
    df["Min"] = df["Min"].astype(float)
    df = df[df["Min"] >= 400].reset_index(drop=True)
    df = df.sort_values(by="Min").reset_index(drop=True)
    df = df[~df["Pos"].isna()]
    df["Nation"] = [x.split(" ")[1].lower() for x in df["Nation"]]
    df["Min"] = [int(x) for x in df["Min"]]
    return df


def get_minutes_all(df):
    df = df.sort_values(by="Min").reset_index(drop=True)
    df["Min"] = [int(x) for x in df["Min"]]
    return df.tail(20)


def minutes(df_pl, df_comps, team_name, matches_pl, matches_comp, fotmob_id):
    df_pl = get_minutes(df_pl)
    df_comps = get_minutes(df_comps)

    plt_minutes(df_pl, team_name, matches_pl, fotmob_id, "pl")
    plt_minutes(df_comps, team_name, matches_comp, fotmob_id, "comps")

    df_pl["club_id"] = fotmob_id
    df_comps["club_id"] = fotmob_id

    return df_pl, df_comps


def minutes_combined(df_minutes_pl, df_minutes_comps):
    df_minutes_pl = get_minutes_all(df_minutes_pl)
    df_minutes_comps = get_minutes_all(df_minutes_comps)

    plt_minutes_all(df_minutes_pl, "pl")
    plt_minutes_all(df_minutes_comps, "comps")
