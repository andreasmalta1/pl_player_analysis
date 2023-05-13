import pandas as pd

from plots.plots_goalkeepers import plt_gk_stats
from constants import LEAGUES


def goalkeepers():
    for lge in LEAGUES:
        lge_name = LEAGUES[lge]["lge_name"].replace(" ", "-")
        fotmob_id = LEAGUES[lge]["fotmob_id"]

        df = pd.read_csv(f"csvs/gks/{lge_name}_gk".lower())
        df_adv = pd.read_csv(f"csvs/gks/{lge_name}_adv_gk".lower())

        mins = df["Min"]
        mps = df["MP"]

        df_adv = df_adv.join(mins)
        df_adv = df_adv.join(mps)

        df = df[df["Min"] >= 900].reset_index(drop=True)
        df_adv = df_adv[df_adv["Min"] >= 900].reset_index(drop=True)

        for i in df.index:
            df.at[i, "Player"] = f"{df.at[i, 'Player']} ({df.at[i, 'MP']})"
            df_adv.at[i, "Player"] = f"{df_adv.at[i, 'Player']} ({df_adv.at[i, 'MP']})"

        df_saves_pct = df[["Player", "Save%"]]
        df_psxg = df_adv[["Player", "PSxG+/-"]]

        plt_gk_stats(df_saves_pct, "Save%", "Saves %", lge, fotmob_id)
        plt_gk_stats(
            df_psxg, "PSxG+/-", "Posts Shots xG - Goals Allowed", lge, fotmob_id
        )
