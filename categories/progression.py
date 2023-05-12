from plots.plots_progression import (
    plt_progression,
    plt_progression_90s,
    plt_progression_combined,
    plt_progression_combined_90s,
    plt_progression_combined_all,
    plt_progression_combined_all_90s,
)


def get_progression(df):
    df = df[["Player", "PrgC", "PrgP"]]
    return df


def get_progression_90s(df):
    df = df[["Player", "Min", "PrgC90", "PrgP90"]]
    df["Min"] = df["Min"].astype(float)
    df = df[df["Min"] >= 1000].reset_index(drop=True)
    df = df[["Player", "PrgC90", "PrgP90"]]
    return df


def progression(df_lge, df_comps, team_name, fotmob_id, lge):
    df_lge_90s = get_progression_90s(df_lge)
    df_comps_90s = get_progression_90s(df_comps)

    df_lge = get_progression(df_lge)
    df_comps = get_progression(df_comps)

    plt_progression(df_lge, team_name, fotmob_id, lge, lge)
    plt_progression(df_comps, team_name, fotmob_id, lge, "comps")

    plt_progression_90s(df_lge_90s, team_name, fotmob_id, lge, lge)
    plt_progression_90s(df_comps_90s, team_name, fotmob_id, lge, "comps")


def progression_combined(df_lge, df_comps, lge):
    df_lge_90s = get_progression_90s(df_lge)
    df_comps_90s = get_progression_90s(df_comps)

    df_lge = get_progression(df_lge)
    df_comps = get_progression(df_comps)

    if lge:
        plt_progression_combined(df_lge, lge, lge)
        plt_progression_combined(df_comps, lge, "comps")
        plt_progression_combined_90s(df_lge_90s, lge, lge)
        plt_progression_combined_90s(df_comps_90s, lge, "comps")
    else:
        plt_progression_combined_all(df_lge, "lge")
        plt_progression_combined_all(df_comps, "comps")
        plt_progression_combined_all_90s(df_lge_90s, "lge")
        plt_progression_combined_all_90s(df_comps_90s, "comps")
