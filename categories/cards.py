from plots.plots_cards import plt_cards, plt_cards_stacked
from constants import LEAGUES


def get_cards(df):
    df = df[["Player", "CrdY", "CrdR"]]
    df = df[~df["CrdY"].isna()]
    df = df[~df["CrdR"].isna()]
    df["CrdY"] = df["CrdY"].astype(int)
    df["CrdR"] = df["CrdR"].astype(int)
    df["Sum"] = df.iloc[:, [1, 2]].sum(axis=1)
    df["Sum"] = df["Sum"].astype(int)
    return df


def cards_combined(df_lge, df_comps, lge):
    df_lge = get_cards(df_lge)
    df_comps = get_cards(df_comps)

    fotmob_id = LEAGUES[lge]["fotmob_id"]

    plt_cards(df_lge, "CrdY", "Yellow", "darkkhaki", fotmob_id, lge, lge)
    plt_cards(df_lge, "CrdR", "Red", "indianred", fotmob_id, lge, lge)
    plt_cards(df_comps, "CrdY", "Yellow", "darkkhaki", fotmob_id, lge, "comps")
    plt_cards(df_comps, "CrdR", "Red", "indianred", fotmob_id, lge, "comps")
    plt_cards_stacked(df_lge, fotmob_id, lge, lge)
    plt_cards_stacked(df_comps, fotmob_id, lge, "comps")
