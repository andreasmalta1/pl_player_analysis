from plots.plots_goals_assists import plt_g_a, plt_g_a_stacked


def get_goals_assists(df):
    df = df[["Player", "MP", "Gls", "Ast", "G+A"]]
    df.columns = ["Player", "MP", "Gls", "Gls90", "Ast", "Ast90", "G+A", "G+A90"]
    df_total = df[["Player", "MP", "Gls", "Ast", "G+A"]]

    for i in df.index:
        df_total.at[
            i, "Player"
        ] = f"{df_total.at[i, 'Player']} ({df_total.at[i, 'MP']})"

    df_90 = df[["Player", "MP", "Gls90", "Ast90", "G+A90"]]

    return df_total, df_90


def goals_and_assists(df_pl, df_comps, team_name, fotmob_id):
    df_pl_total, df_pl_90 = get_goals_assists(df_pl)
    df_pl_total.drop(df_pl_total.tail(2).index, inplace=True)
    df_pl_90.drop(df_pl_90.tail(2).index, inplace=True)
    df_comps_total, df_comps_90 = get_goals_assists(df_comps)

    plt_g_a(df_pl_total, "Gls", "Goals", team_name, "#C4961A", fotmob_id, "pl")
    plt_g_a(df_pl_total, "Ast", "Assists", team_name, "cadetblue", fotmob_id, "pl")
    plt_g_a_stacked(df_pl_total, "G+A", "Goals + Assists", team_name, fotmob_id, "pl")

    plt_g_a(df_pl_90, "Gls90", "Goals / 90", team_name, "#C4961A", fotmob_id, "pl")
    plt_g_a(df_pl_90, "Ast90", "Assists / 90", team_name, "cadetblue", fotmob_id, "pl")
    plt_g_a_stacked(
        df_pl_90, "G+A90", "Goals + Assists / 90", team_name, fotmob_id, "pl"
    )

    plt_g_a(df_comps_total, "Gls", "Goals", team_name, "#C4961A", fotmob_id, "comps")
    plt_g_a(
        df_comps_total, "Ast", "Assists", team_name, "cadetblue", fotmob_id, "comps"
    )
    plt_g_a_stacked(
        df_comps_total,
        "G+A",
        "Goals + Assists",
        team_name,
        fotmob_id,
        "comps",
    )

    plt_g_a(
        df_comps_90, "Gls90", "Goals / 90", team_name, "#C4961A", fotmob_id, "comps"
    )
    plt_g_a(
        df_comps_90, "Ast90", "Assists / 90", team_name, "cadetblue", fotmob_id, "comps"
    )
    plt_g_a_stacked(
        df_comps_90, "G+A90", "Goals + Assists / 90", team_name, fotmob_id, "comps"
    )

    return df_pl_total, df_pl_90, df_comps_total, df_comps_90


def goals_and_assists_combined(
    df_goals_pl, df_goals_comps, df_goals_90_pl, df_goals_90_comps
):
    plt_g_a(
        df=df_goals_pl,
        column_name="Gls",
        label="Goals",
        plot_color="#C4961A",
        fotmob_id=47,
        competition="pl",
    )
    plt_g_a(
        df=df_goals_pl,
        column_name="Ast",
        label="Assists",
        plot_color="cadetblue",
        fotmob_id=47,
        competition="pl",
    )
    plt_g_a_stacked(
        df=df_goals_pl,
        column_name="G+A",
        label="Goals + Assists",
        fotmob_id=47,
        competition="pl",
    )

    plt_g_a(
        df=df_goals_90_pl,
        column_name="Gls90",
        label="Goals / 90",
        plot_color="#C4961A",
        fotmob_id=47,
        competition="pl",
    )
    plt_g_a(
        df=df_goals_90_pl,
        column_name="Ast90",
        label="Assists / 90",
        plot_color="cadetblue",
        fotmob_id=47,
        competition="pl",
    )
    plt_g_a_stacked(
        df=df_goals_90_pl,
        column_name="G+A90",
        label="Goals + Assists / 90",
        fotmob_id=47,
        competition="pl",
    )

    plt_g_a(
        df=df_goals_comps,
        column_name="Gls",
        label="Goals",
        plot_color="#C4961A",
        fotmob_id=47,
        competition="comps",
    )
    plt_g_a(
        df=df_goals_comps,
        column_name="Ast",
        label="Assists",
        plot_color="cadetblue",
        fotmob_id=47,
        competition="comps",
    )
    plt_g_a_stacked(
        df=df_goals_comps,
        column_name="G+A",
        label="Goals + Assists",
        fotmob_id=47,
        competition="comps",
    )

    plt_g_a(
        df=df_goals_90_comps,
        column_name="Gls90",
        label="Goals / 90",
        plot_color="#C4961A",
        fotmob_id=47,
        competition="comps",
    )
    plt_g_a(
        df=df_goals_90_comps,
        column_name="Ast90",
        label="Assists / 90",
        plot_color="cadetblue",
        fotmob_id=47,
        competition="comps",
    )
    plt_g_a_stacked(
        df=df_goals_90_comps,
        column_name="G+A90",
        label="Goals + Assists / 90",
        fotmob_id=47,
        competition="comps",
    )
