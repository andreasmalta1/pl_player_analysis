from plots.plots_minutes import plt_minutes, plt_minutes_all


def get_num_matches(df):
    df = df["Result"].tail(1)
    total_games = df.iloc[0].split("-")
    num_games = 0
    for value in total_games:
        num_games += int(value)

    return num_games


def get_minutes(df):
    df = df[["Player", "Nation", "Pos", "Age", "Min", "MP", "Starts", "90s", "club_id"]]
    df["Min"] = df["Min"].astype(float)
    df = df[df["Min"] >= 400].reset_index(drop=True)
    df = df.sort_values(by="Min").reset_index(drop=True)
    df = df[~df["Pos"].isna()]
    df["Nation"] = [x.split(" ")[1].lower() for x in df["Nation"]]
    df["Min"] = [int(x) for x in df["Min"]]
    return df


def minutes(df_lge, df_comps, df_lge_mth, df_comps_mth, team_name, fotmob_id, lge):
    df_lge = get_minutes(df_lge)
    df_comps = get_minutes(df_comps)
    mth_league = get_num_matches(df_lge_mth)
    mth_comps = get_num_matches(df_comps_mth)

    plt_minutes(df_lge, team_name, mth_league, fotmob_id, lge, lge)
    plt_minutes(df_comps, team_name, mth_comps, fotmob_id, lge, "comps")


def minutes_combined(df_lge, df_comps, lge):
    df_lge = get_minutes(df_lge)
    df_comps = get_minutes(df_comps)

    plt_minutes_all(df_lge.tail(20), lge, lge)
    plt_minutes_all(df_comps.tail(20), lge, "comps")
