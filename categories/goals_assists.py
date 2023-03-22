from plots.plots_goals_assists import (
    plt_g_a,
    plt_g_a_all,
    plt_g_a_lges,
    plt_g_a_all_lges,
)
from constants import LEAGUES


def get_goals_assists(df):
    df_total = df[["Player", "MP", "Gls", "Ast", "G+A"]]

    for i in df_total.index:
        df_total.at[
            i, "Player"
        ] = f"{df_total.at[i, 'Player']} ({df_total.at[i, 'MP']})"

    df_90 = df[["Player", "MP", "Min", "Gls90", "Ast90", "G+A90"]]
    df_90["Min"] = df_90["Min"].astype(float)
    df_90 = df_90[df_90["Min"] >= 900].reset_index(drop=True)

    for i in df_90.index:
        df_90.at[i, "Player"] = f"{df_90.at[i, 'Player']} ({df_90.at[i, 'MP']})"

    return df_total, df_90


def goals_and_assists(df_lge, df_comps, team_name, fotmob_id, lge):
    df_lge_total, df_lge_90 = get_goals_assists(df_lge)
    df_comps_total, df_comps_90 = get_goals_assists(df_comps)

    plt_g_a(df_lge_total, "Gls", "Goals", team_name, "#C4961A", fotmob_id, lge, lge)
    plt_g_a(df_lge_total, "Ast", "Assists", team_name, "cadetblue", fotmob_id, lge, lge)
    plt_g_a_all(df_lge_total, "G+A", "Goals + Assists", team_name, fotmob_id, lge, lge)

    plt_g_a(df_lge_90, "Gls90", "Goals / 90", team_name, "#C4961A", fotmob_id, lge, lge)
    plt_g_a(
        df_lge_90, "Ast90", "Assists / 90", team_name, "cadetblue", fotmob_id, lge, lge
    )
    plt_g_a_all(
        df_lge_90, "G+A90", "Goals + Assists / 90", team_name, fotmob_id, lge, lge
    )

    plt_g_a(
        df_comps_total, "Gls", "Goals", team_name, "#C4961A", fotmob_id, lge, "comps"
    )
    plt_g_a(
        df_comps_total,
        "Ast",
        "Assists",
        team_name,
        "cadetblue",
        fotmob_id,
        lge,
        "comps",
    )
    plt_g_a_all(
        df_comps_total,
        "G+A",
        "Goals + Assists",
        team_name,
        fotmob_id,
        lge,
        "comps",
    )

    plt_g_a(
        df_comps_90,
        "Gls90",
        "Goals / 90",
        team_name,
        "#C4961A",
        fotmob_id,
        lge,
        "comps",
    )
    plt_g_a(
        df_comps_90,
        "Ast90",
        "Assists / 90",
        team_name,
        "cadetblue",
        fotmob_id,
        lge,
        "comps",
    )
    plt_g_a_all(
        df_comps_90, "G+A90", "Goals + Assists / 90", team_name, fotmob_id, lge, "comps"
    )


def goals_and_assists_combined(df_lge, df_comps, lge):
    df_lge_total, df_lge_90 = get_goals_assists(df_lge)
    df_comps_total, df_comps_90 = get_goals_assists(df_comps)
    if lge:
        fotmob_id = LEAGUES[lge]["fotmob_id"]
        plt_g_a(df_lge_total, "Gls", "Goals", None, "#C4961A", fotmob_id, lge, lge)
        plt_g_a(df_lge_total, "Ast", "Assists", None, "cadetblue", fotmob_id, lge, lge)
        plt_g_a_all(df_lge_total, "G+A", "Goals + Assists", None, fotmob_id, lge, lge)

        plt_g_a(df_lge_90, "Gls90", "Goals / 90", None, "#C4961A", fotmob_id, lge, lge)
        plt_g_a(
            df_lge_90, "Ast90", "Assists / 90", None, "cadetblue", fotmob_id, lge, lge
        )
        plt_g_a_all(
            df_lge_90, "G+A90", "Goals + Assists / 90", None, fotmob_id, lge, lge
        )

        plt_g_a(
            df_comps_total, "Gls", "Goals", None, "#C4961A", fotmob_id, lge, "comps"
        )
        plt_g_a(
            df_comps_total, "Ast", "Assists", None, "cadetblue", fotmob_id, lge, "comps"
        )
        plt_g_a_all(
            df_comps_total, "G+A", "Goals + Assists", None, fotmob_id, lge, "comps"
        )
        plt_g_a(
            df_comps_90, "Gls90", "Goals / 90", None, "#C4961A", fotmob_id, lge, "comps"
        )
        plt_g_a(
            df_comps_90,
            "Ast90",
            "Assists / 90",
            None,
            "cadetblue",
            fotmob_id,
            lge,
            "comps",
        )
        plt_g_a_all(
            df_comps_90, "G+A90", "Goals + Assists / 90", None, fotmob_id, lge, "comps"
        )

    else:
        plt_g_a_lges(df_lge_total, "Gls", "Goals", "#C4961A", "lge")
        plt_g_a_lges(df_lge_total, "Ast", "Assists", "cadetblue", "lge")
        plt_g_a_all_lges(df_lge_total, "G+A", "Goals + Assists", "lge")

        plt_g_a_lges(df_lge_90, "Gls90", "Goals / 90", "#C4961A", "lge")
        plt_g_a_lges(df_lge_90, "Ast90", "Assists / 90", "cadetblue", "lge")
        plt_g_a_all_lges(df_lge_90, "G+A90", "Goals + Assists / 90", "lge")

        plt_g_a_lges(df_comps_total, "Gls", "Goals", "#C4961A", "comps")
        plt_g_a_lges(df_comps_total, "Ast", "Assists", "cadetblue", "comps")
        plt_g_a_all_lges(df_comps_total, "G+A", "Goals + Assists", "comps")

        plt_g_a_lges(df_comps_90, "Gls90", "Goals / 90", "#C4961A", "comps")
        plt_g_a_lges(
            df_comps_90,
            "Ast90",
            "Assists / 90",
            "cadetblue",
            "comps",
        )
        plt_g_a_all_lges(df_comps_90, "G+A90", "Goals + Assists / 90", "comps")
