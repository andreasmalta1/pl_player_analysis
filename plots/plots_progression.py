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

    # texts = []

    # for index, row in df.iterrows():
    #     if row["PrgP"] > passes_limit or row["PrgC"] > carries_limit:
    #         # ax.annotate(row["Player"], (row["PrgP"] + 0.2, row["PrgC"] + 1))
    #         texts.append(ax.annotate(row["PrgP"], row["PrgC"], row["Player"]))

    # adjust_text(
    #     texts,
    #     only_move={"points": "y", "texts": "y"},
    #     arrowprops=dict(arrowstyle="->", color="r", lw=0.5),
    # )

    """
    import matplotlib.pyplot as plt
    from adjustText import adjust_text
    import numpy as np
    together = [(0, 1.0, 0.4), (25, 1.0127692669427917, 0.41), (50, 1.016404709797609, 0.41), (75, 1.1043426359673716, 0.42), (100, 1.1610446924342996, 0.44), (125, 1.1685687930691457, 0.43), (150, 1.3486407784550272, 0.45), (250, 1.4013999168008104, 0.45)]
    together.sort()

    text = [x for (x,y,z) in together]
    eucs = [y for (x,y,z) in together]
    covers = [z for (x,y,z) in together]

    p1 = plt.plot(eucs,covers,color="black", alpha=0.5)
    texts = []
    for x, y, s in zip(eucs, covers, text):
        texts.append(plt.text(x, y, s))

    plt.xlabel("Proportional Euclidean Distance")
    plt.ylabel("Percentage Timewindows Attended")
    plt.title("Test plot")
    adjust_text(texts, only_move={'points':'y', 'texts':'y'}, arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
    plt.show()
    """

    logo_ax = fig.add_axes([0.88, 0.77, 0.1, 0.1])
    ax_logo(fotmob_id, logo_ax)

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/progression/{comp}/{team_name.replace('-', '_').lower()}.png",
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

    texts = []

    for index, row in df.iterrows():
        if row["PrgP"] > passes_limit or row["PrgC"] > carries_limit:
            # ax.annotate(row["Player"], (row["PrgP"] + 0.2, row["PrgC"] + 1))
            texts.append(plt.text(row["PrgP"], row["PrgC"], row["Player"]))

    adjust_text(
        texts,
        only_move={"points": "y", "texts": "y"},
        arrowprops=dict(arrowstyle="->", color="r", lw=0.5),
    )

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
