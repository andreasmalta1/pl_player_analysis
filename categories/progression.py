from plots.plots_progression import (
    plt_progression,
    plt_progression_combined,
    plt_progression_combined_all,
)


def get_progression(df):
    df = df[["Player", "PrgC", "PrgP"]]
    return df


def progression(df_lge, df_comps, team_name, fotmob_id, lge):
    df_lge = get_progression(df_lge)
    df_comps = get_progression(df_comps)

    plt_progression(df_lge, team_name, fotmob_id, lge, lge)
    plt_progression(df_comps, team_name, fotmob_id, lge, "comps")


def progression_combined(df_lge, df_comps, lge):
    df_lge = get_progression(df_lge)
    df_comps = get_progression(df_comps)

    if lge:
        plt_progression_combined(df_lge, lge, lge)
        plt_progression_combined(df_comps, lge, "comps")
    else:
        plt_progression_combined_all(df_lge, "lge")
        plt_progression_combined_all(df_comps, "comps")
