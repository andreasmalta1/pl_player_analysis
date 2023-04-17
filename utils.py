import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image

from constants import AGGREGATOR, NINETY_COLUMNS, NATION_COLOURS


def drop_rows(df, column, value):
    for i in df.index:
        if df.at[i, column] == value:
            df = df.drop([i])
    return df


def remove_duplicates(df):
    duplicate_rows = df[df.duplicated(["Player"])]
    df.drop_duplicates(subset=["Player"], inplace=True)
    df = (
        pd.concat([df, duplicate_rows])
        .groupby(["Player", "Nation", "Age"], as_index=False)
        .agg(AGGREGATOR)
    )

    for column_name in NINETY_COLUMNS:
        col_name = column_name[:-2]
        if col_name in df.columns:
            for i in df.index:
                df.at[i, column_name] = round(
                    (int(df.at[i, col_name]) / float(df.at[i, "90s"])),
                    2,
                )
    return df


def get_info(url):
    html = pd.read_html(url, header=0)
    df = html[0]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    return df


def ax_logo(logo_id, ax, league=False, alpha=1):
    url = "https://images.fotmob.com/image_resources/logo/teamlogo/"
    if league:
        url = "https://images.fotmob.com/image_resources/logo/leaguelogo/"
    icon = Image.open(urllib.request.urlopen(f"{url}{logo_id}.png"))
    ax.imshow(icon, alpha=alpha)
    ax.axis("off")
    return ax


def annotate_axis(ax):
    ax.annotate(
        "Stats from fbref.com",
        (0, 0),
        (0, -20),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    ax.annotate(
        "Data Viz by @plvizstats || u/plvizstats",
        (0, 0),
        (0, -30),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    return ax


def remove_plot_border(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)


def save_figure(fig_name, dpi, transparency, face_color, bbox):
    plt.savefig(
        fig_name,
        dpi=dpi,
        transparent=transparency,
        facecolor=face_color,
        bbox_inches=bbox,
    )


def minutes_battery(ax, minutes, num_games):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    pct = minutes / (90 * num_games)
    ax.barh([0.5], [1], fc="#EFE9E6", ec="black", height=0.35)
    ax.barh([0.5], [pct], fc="#00529F", height=0.35)
    if pct > 0.3:
        ax.annotate(
            xy=(pct, 0.5),
            text=f"{pct:.0%}",
            xytext=(-8, 0),
            textcoords="offset points",
            weight="bold",
            color="#EFE9E6",
            va="center",
            ha="center",
            size=5,
        )
    else:
        ax.annotate(
            xy=(pct + 0.01, 0.5),
            text=f"{pct:.0%}",
            weight="bold",
            color="#00529F",
            va="center",
            ha="left",
            size=5,
        )
    ax.set_axis_off()
    return ax


def get_nation_colours(teams):
    teams = teams.values.tolist()
    colors = []
    for team in teams:
        if team in NATION_COLOURS:
            colors.append(NATION_COLOURS[team])
        else:
            pass
            print(team)

    return colors
