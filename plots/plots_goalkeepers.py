import matplotlib.pyplot as plt
import os

from utils import annotate_axis, ax_logo, save_figure, remove_plot_border
from constants import LEAGUES


def plt_gk_stats(df, col, label, fotmob_id):
    league = True
    file_name = f"gks_{col.lower()}"
    title = f"{label} Premier League 22/23"

    df = df.sort_values(col)

    print(df)

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
    ax.set_xlabel(f"{label}", fontweight="bold")
    ax.barh(df["Player"], df[col], align="center")
    pos_increment_value = df[col].iloc[-1] * 0.02
    for index, value in enumerate(df[col]):
        if value > 0:
            annotation_pos = value + pos_increment_value
        elif value < -10:
            annotation_pos = value - pos_increment_value + 0.35
        else:
            annotation_pos = value - pos_increment_value - 1.5
        plt.text(
            annotation_pos,
            index,
            str(value),
            color="#000000",
            va="center",
            fontweight="bold",
        )

    # logo_ax = fig.add_axes([0.80, 0.1, 0.15, 0.15])
    logo_ax = fig.add_axes([0.65, 0.2, 0.2, 0.2])
    ax_logo(fotmob_id, logo_ax, league)

    annotate_axis(ax)

    save_figure(
        f"figures/epl/gks/{file_name}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
