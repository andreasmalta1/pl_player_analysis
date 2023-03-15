from plots.plots_goals_assists import plt_g_a, plt_g_a_stacked


def get_goals_assists(df):
    df = df[["Player", "MP", "Gls", "Ast", "G+A"]]
    df.columns = ["Player", "MP", "Gls", "xG", "Ast", "xA", "G+A", "xG+xA"]
    df = df[["Player", "MP", "Gls", "Ast", "G+A"]]

    for i in df.index:
        df.at[i, "Player"] = f"{df.at[i, 'Player']} ({df.at[i, 'MP']})"
    return df


def goals_and_assists(df_pl, df_comps, team_name, fotmob_id):
    df_pl = get_goals_assists(df_pl)
    df_pl.drop(df_pl.tail(2).index, inplace=True)
    df_comps = get_goals_assists(df_comps)

    plt_g_a(df_pl, "Gls", "Goals", team_name, "#C4961A", fotmob_id, "pl")
    plt_g_a(df_pl, "Ast", "Assists", team_name, "cadetblue", fotmob_id, "pl")
    plt_g_a_stacked(df_pl, "G+A", "Goals + Assists", team_name, fotmob_id, "pl")

    plt_g_a(df_comps, "Gls", "Goals", team_name, "#C4961A", fotmob_id, "comps")
    plt_g_a(df_comps, "Ast", "Assists", team_name, "cadetblue", fotmob_id, "comps")
    plt_g_a_stacked(
        df_comps,
        "G+A",
        "Goals + Assists",
        team_name,
        fotmob_id,
        "comps",
    )

    return df_pl, df_comps


def goals_and_assists_combined(df_goals_pl, df_goals_comps):
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
