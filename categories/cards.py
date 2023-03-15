from plots.plots_cards import plt_cards, plt_cards_stacked


def get_cards(df):
    df = df[["Player", "CrdY", "CrdR"]]
    df = df[~df["CrdY"].isna()]
    df = df[~df["CrdR"].isna()]
    df["CrdY"] = df["CrdY"].astype(int)
    df["CrdR"] = df["CrdR"].astype(int)
    df["Sum"] = df.iloc[:, [1, 2]].sum(axis=1)
    df["Sum"] = df["Sum"].astype(int)
    return df


def get_cards_info(df_pl, df_comps):
    df_pl = get_cards(df_pl)
    df_pl.drop(df_pl.tail(2).index, inplace=True)
    df_comps = get_cards(df_comps)

    return df_pl, df_comps


def cards_combined(df_pl, df_comps):
    plt_cards(df_pl, "CrdY", "Yellow", "darkkhaki", "pl")
    plt_cards(df_pl, "CrdR", "Red", "indianred", "pl")
    plt_cards(df_comps, "CrdY", "Yellow", "darkkhaki", "comps")
    plt_cards(df_comps, "CrdR", "Red", "indianred", "comps")
    plt_cards_stacked(df_pl, "Disciplinary Record", "pl")
    plt_cards_stacked(df_comps, "Disciplinary Record", "comps")
