import matplotlib.pyplot as plt

from utils import annotate_axis, ax_logo, save_figure, remove_plot_border
from constants import LEAGUES


def plt_g_a(df, column_name, label, team_name, plot_color, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    league = False

    if label == "Goals" or label == "Goals / 90":
        descriptor = "Scored"
    if label == "Assists" or label == "Assists / 90":
        descriptor = "Provided"

    if team_name:
        file_name = f"{team_name.replace('-', '_').lower()}_{column_name.lower()}"
        title = f"{team_name.replace('-', ' ')} {label} {descriptor} {comp_description} 22/23"
    else:
        file_name = f"all_{column_name.lower()}"
        title = f"{label} {descriptor} {comp_description} 22/23"

    df = df[["Player", column_name]]
    df = df[~df[column_name].isna()]
    if "90" not in column_name:
        df[column_name] = df[column_name].astype(int)
    else:
        df[column_name] = df[column_name].astype(float)
    df = df[df[column_name] != 0]
    df = df.sort_values(column_name)

    if fotmob_id == LEAGUES[lge]["fotmob_id"]:
        df = df.tail(30)
        league = True

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    remove_plot_border(ax)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_ylabel("Player (Matches Played)", fontweight="bold")
    ax.set_xlabel(f"{label} {descriptor}", fontweight="bold")
    ax.barh(df["Player"], df[column_name], align="center", color=plot_color)
    increment_value = df[column_name].iloc[0] * 0.02
    for index, value in enumerate(df[column_name]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    logo_ax = fig.add_axes([0.60, 0.2, 0.2, 0.2])
    ax_logo(fotmob_id, logo_ax, league)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/{column_name.lower()}/{comp}/{file_name}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_g_a_all(df, column_name, label, team_name, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    league = False

    descriptor = "Leaderboard"

    if team_name:
        file_name = f"{team_name.replace('-', '_').lower()}_{column_name.lower()}"
        title = f"{team_name.replace('-', ' ')} {label} {descriptor} {comp_description} 22/23"
    else:
        file_name = f"all_{column_name.lower()}"
        title = f"{label} {descriptor} {comp_description} 22/23"

    df = df[~df[column_name].isna()]
    if "90" not in column_name:
        df[column_name] = df[column_name].astype(int)
        df["Gls"] = df["Gls"].astype(int)
        df["Ast"] = df["Ast"].astype(int)
    else:
        df[column_name] = df[column_name].astype(float)
        df["Gls90"] = df["Gls90"].astype(float)
        df["Ast90"] = df["Ast90"].astype(float)

    df = df[df[column_name] != 0]
    if "G+A" in column_name:
        if "90" not in column_name:
            df = df.sort_values([column_name, "Gls"])
        else:
            df = df.sort_values([column_name, "Gls90"])
    else:
        df = df.sort_values(column_name)

    if fotmob_id == LEAGUES[lge]["fotmob_id"]:
        df = df.tail(30)
        league = True

    players = df.Player.values.tolist()
    if "90" not in column_name:
        goals = df.Gls.values.tolist()
        assists = df.Ast.values.tolist()
    else:
        goals = df.Gls90.values.tolist()
        assists = df.Ast90.values.tolist()

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    remove_plot_border(ax)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_ylabel("Player (Matches Played)", fontweight="bold")
    ax.set_xlabel(f"{label} {descriptor}", fontweight="bold")
    ax.barh(players, goals, align="center", color="#C4961A", label="Goals")
    ax.barh(
        players, assists, align="center", left=goals, color="cadetblue", label="Assists"
    )

    increment_value = df[column_name].iloc[0] * 0.02
    for index, value in enumerate(df[column_name]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    if "90" not in column_name:
        for index, value in enumerate(goals):
            if value == 0:
                continue
            plt.text(
                value / 2,
                index,
                str(value),
                color="#000000",
                va="center",
                fontweight="bold",
            )

        for index, value in enumerate(assists):
            if value == 0:
                continue
            plt.text(
                goals[index] + (value / 2),
                index,
                str(value),
                color="#000000",
                va="center",
                fontweight="bold",
            )

    ax.legend(loc="lower right")

    logo_ax = fig.add_axes([0.60, 0.2, 0.2, 0.2])
    ax_logo(fotmob_id, logo_ax, league)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/{column_name.lower()}/{comp}/{file_name}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_g_a_lges(df, column_name, label, plot_color, comp):
    if comp == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "League Games"

    if label == "Goals" or label == "Goals / 90":
        descriptor = "Scored"
    if label == "Assists" or label == "Assists / 90":
        descriptor = "Provided"

    file_name = f"all_{column_name.lower()}_{comp}"
    title = f"Top 5 Leagues {label} {descriptor} {comp_description} 22/23"

    df = df[["Player", column_name]]
    df = df[~df[column_name].isna()]
    if "90" not in column_name:
        df[column_name] = df[column_name].astype(int)
    else:
        df[column_name] = df[column_name].astype(float)
    df = df[df[column_name] != 0]
    df = df.sort_values(column_name)
    df = df.tail(30)

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    remove_plot_border(ax)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_ylabel("Player (Matches Played)", fontweight="bold")
    ax.set_xlabel(f"{label} {descriptor}", fontweight="bold")
    ax.barh(df["Player"], df[column_name], align="center", color=plot_color)
    increment_value = df[column_name].iloc[0] * 0.02
    for index, value in enumerate(df[column_name]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    annotate_axis(ax)

    save_figure(
        f"figures/combined/{column_name.lower()}/{file_name}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_g_a_all_lges(df, column_name, label, comp):
    if comp == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "League Games"

    descriptor = "Leaderboard"

    file_name = f"all_{column_name.lower()}_{comp}"
    title = f"Top 5 Leagues {label} {descriptor} {comp_description} 22/23"

    df = df[~df[column_name].isna()]
    if "90" not in column_name:
        df[column_name] = df[column_name].astype(int)
        df["Gls"] = df["Gls"].astype(int)
        df["Ast"] = df["Ast"].astype(int)
    else:
        df[column_name] = df[column_name].astype(float)
        df["Gls90"] = df["Gls90"].astype(float)
        df["Ast90"] = df["Ast90"].astype(float)

    df = df[df[column_name] != 0]
    if "G+A" in column_name:
        if "90" not in column_name:
            df = df.sort_values([column_name, "Gls"])
        else:
            df = df.sort_values([column_name, "Gls90"])
    else:
        df = df.sort_values(column_name)
    df = df.tail(30)

    players = df.Player.values.tolist()
    if "90" not in column_name:
        goals = df.Gls.values.tolist()
        assists = df.Ast.values.tolist()
    else:
        goals = df.Gls90.values.tolist()
        assists = df.Ast90.values.tolist()

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    remove_plot_border(ax)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_ylabel("Player (Matches Played)", fontweight="bold")
    ax.set_xlabel(f"{label} {descriptor}", fontweight="bold")
    ax.barh(players, goals, align="center", color="#C4961A", label="Goals")
    ax.barh(
        players, assists, align="center", left=goals, color="cadetblue", label="Assists"
    )

    increment_value = df[column_name].iloc[0] * 0.02
    for index, value in enumerate(df[column_name]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    if "90" not in column_name:
        for index, value in enumerate(goals):
            if value == 0:
                continue
            plt.text(
                value / 2,
                index,
                str(value),
                color="#000000",
                va="center",
                fontweight="bold",
            )

        for index, value in enumerate(assists):
            if value == 0:
                continue
            plt.text(
                goals[index] + (value / 2),
                index,
                str(value),
                color="#000000",
                va="center",
                fontweight="bold",
            )

    ax.legend(loc="lower right")

    annotate_axis(ax)

    save_figure(
        f"figures/combined/{column_name.lower()}/{file_name}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
