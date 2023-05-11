import matplotlib.pyplot as plt
from adjustText import adjust_text

from utils import annotate_axis, ax_logo, save_figure, remove_plot_border
from constants import LEAGUES


def plt_progression(df, team_name, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    passes_limit = df.PrgP.max() * 0.6
    carries_limit = df.PrgC.max() * 0.6

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(
        f"{team_name.replace('-', ' ')} Progression Passes V Carries {comp_description} 22/23",
        fontweight="bold",
        fontsize=12,
    )

    ax.set_ylabel("Progressive Carries", fontweight="bold")
    ax.set_xlabel("Progressive Passes", fontweight="bold")
    ax.scatter(df["PrgP"], df["PrgC"], color="#FF7F0E")

    for index, row in df.iterrows():
        if row["PrgP"] > passes_limit or row["PrgC"] > carries_limit:
            ax.annotate(row["Player"], (row["PrgP"] + 0.2, row["PrgC"] + 1))

    logo_ax = fig.add_axes([0.88, 0.77, 0.1, 0.1])
    ax_logo(fotmob_id, logo_ax, alpha=0.5)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/progression/{comp}/{team_name.replace('-', '_').lower()}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_progression_90s(df, team_name, fotmob_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    passes_limit = df.PrgP90.max() * 0.6
    carries_limit = df.PrgC90.max() * 0.6

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(
        f"{team_name.replace('-', ' ')} Progression Passes V Carries Per 90 {comp_description} 22/23",
        fontweight="bold",
        fontsize=12,
    )

    ax.set_ylabel("Progressive Carries Per 90", fontweight="bold")
    ax.set_xlabel("Progressive Passes Per 90", fontweight="bold")
    ax.scatter(df["PrgP90"], df["PrgC90"], color="#FF7F0E")

    for index, row in df.iterrows():
        if row["PrgP90"] > passes_limit or row["PrgC90"] > carries_limit:
            ax.annotate(row["Player"], (row["PrgP90"] + 0.3, row["PrgC90"]))

    logo_ax = fig.add_axes([0.88, 0.77, 0.1, 0.1])
    ax_logo(fotmob_id, logo_ax, alpha=0.5)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/progression/{comp}/{team_name.replace('-', '_').lower()}_90.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_progression_combined(df, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")
    lge_id = LEAGUES.get(lge).get("fotmob_id")

    passes_limit = df.PrgP.max() * 0.6
    carries_limit = df.PrgC.max() * 0.6

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(
        f"Progression Passes V Carries {comp_description} 22/23",
        fontweight="bold",
        fontsize=12,
    )

    ax.set_ylabel("Progressive Carries", fontweight="bold")
    ax.set_xlabel("Progressive Passes", fontweight="bold")
    ax.scatter(df["PrgP"], df["PrgC"], color="#FF7F0E")

    for index, row in df.iterrows():
        if row["PrgP"] > passes_limit or row["PrgC"] > carries_limit:
            ax.annotate(row["Player"], (row["PrgP"] + 0.2, row["PrgC"] + 1))

    logo_ax = fig.add_axes([0.88, 0.77, 0.1, 0.1])
    ax_logo(lge_id, logo_ax, True)

    annotate_axis(ax)

    if not lge:
        lge = "combined"

    save_figure(
        f"figures/{lge}/progression/{comp}/all_progression.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_progression_combined_all(df, comp):
    if comp == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "League Games"

    passes_limit = df.PrgP.max() * 0.6
    carries_limit = df.PrgC.max() * 0.6

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()
    ax.set_facecolor("#EFE9E6")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(
        f"Progression Passes V Carries {comp_description} 22/23",
        fontweight="bold",
        fontsize=12,
    )

    ax.set_ylabel("Progressive Carries", fontweight="bold")
    ax.set_xlabel("Progressive Passes", fontweight="bold")
    ax.scatter(df["PrgP"], df["PrgC"], color="#FF7F0E")

    for index, row in df.iterrows():
        if row["PrgP"] > passes_limit or row["PrgC"] > carries_limit:
            ax.annotate(row["Player"], (row["PrgP"] + 0.2, row["PrgC"] + 1))

    annotate_axis(ax)

    save_figure(
        f"figures/combined/progression/all_progression_{comp}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
