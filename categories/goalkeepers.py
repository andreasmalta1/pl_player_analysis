import pandas as pd
from plots.plots_goalkeepers import plt_gk_stats


def goalkeepers():
    df = pd.read_csv(f"csvs/epl/goalkeepers/epl_gks.csv")
    df_advanced = pd.read_csv(f"csvs/epl/goalkeepers/epl_gks_advanced.csv")

    mins = df["Min"]
    mps = df["MP"]

    df_advanced = df_advanced.join(mins)
    df_advanced = df_advanced.join(mps)

    df = df[df["Min"] >= 900].reset_index(drop=True)
    df_advanced = df_advanced[df_advanced["Min"] >= 900].reset_index(drop=True)

    for i in df.index:
        df.at[i, "Player"] = f"{df.at[i, 'Player']} ({df.at[i, 'MP']})"
        df_advanced.at[
            i, "Player"
        ] = f"{df_advanced.at[i, 'Player']} ({df_advanced.at[i, 'MP']})"

    df_saves_pct = df[["Player", "Save%"]]
    df_psxg = df_advanced[["Player", "PSxG-GA"]]

    plt_gk_stats(df_saves_pct, "Save%", "Saves %", 47)
    plt_gk_stats(df_psxg, "PSxG-GA", "Posts Shots xG - Goals Allowed", 47)
