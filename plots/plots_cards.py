import matplotlib.pyplot as plt

from utils import annotate_axis, ax_logo, save_figure, remove_plot_border
from constants import LEAGUES


def plt_cards(df, column_name, label, plot_color, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    title = f"{label} Cards {comp_description} 23/24"

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
    ax.set_xlabel(f"{label} Cards", fontweight="bold")
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

    logo_ax = fig.add_axes([0.68, 0.2, 0.2, 0.2])
    ax_logo(fotmob_id, logo_ax, True)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/cards/{comp}/{label.lower()}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_cards_all(df, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    label = "Disciplinary Record"
    title = f"{label} {comp_description} 23/24"

    df = df[df["Sum"] != 0]
    df = df.sort_values(["Sum", "CrdR"])
    df = df.tail(30)

    players = df.Player.values.tolist()
    yellows = df.CrdY.values.tolist()
    reds = df.CrdR.values.tolist()

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_xlabel(f"Yellow & Red Cards", fontweight="bold")
    ax.barh(players, yellows, align="center", color="darkkhaki", label="Yellows")
    ax.barh(
        players, reds, align="center", left=yellows, color="indianred", label="Reds"
    )

    increment_value = df["Sum"].iloc[0] * 0.02
    for index, value in enumerate(df["Sum"]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    for index, value in enumerate(yellows):
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

    for index, value in enumerate(reds):
        if value == 0:
            continue
        plt.text(
            yellows[index] + (value / 2),
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    ax.legend(loc="lower right")

    logo_ax = fig.add_axes([0.68, 0.2, 0.2, 0.2])
    ax_logo(fotmob_id, logo_ax, True)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/cards/{comp}/all_cards.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_cards_lges(df, column_name, label, plot_color, comp):
    if comp == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "League Games"

    title = f"Top 5 Leagues {label} Cards {comp_description} 23/24"

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
    ax.set_xlabel(f"{label} Cards", fontweight="bold")
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
        f"figures/combined/cards/{label.lower()}_{comp}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_cards_all_lges(df, comp):
    if comp == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "League Games"

    label = "Disciplinary Record"
    title = f"Top 5 Leagues {label} Cards {comp_description} 23/24"

    df = df[df["Sum"] != 0]
    df = df.sort_values(["Sum", "CrdR"])
    df = df.tail(30)

    players = df.Player.values.tolist()
    yellows = df.CrdY.values.tolist()
    reds = df.CrdR.values.tolist()

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.set_title(
        title,
        fontweight="bold",
        fontsize=12,
    )
    ax.set_xlabel(f"Yellow & Red Cards", fontweight="bold")
    ax.barh(players, yellows, align="center", color="darkkhaki", label="Yellows")
    ax.barh(
        players, reds, align="center", left=yellows, color="indianred", label="Reds"
    )

    increment_value = df["Sum"].iloc[0] * 0.02
    for index, value in enumerate(df["Sum"]):
        plt.text(
            value + increment_value,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    for index, value in enumerate(yellows):
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

    for index, value in enumerate(reds):
        if value == 0:
            continue
        plt.text(
            yellows[index] + (value / 2),
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    ax.legend(loc="lower right")

    annotate_axis(ax)

    save_figure(
        f"figures/combined/cards/all_cards_{comp}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
