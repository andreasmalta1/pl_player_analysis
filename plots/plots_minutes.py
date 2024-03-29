import matplotlib.pyplot as plt

from utils import annotate_axis, ax_logo, minutes_battery, save_figure
from constants import LEAGUES


def plt_minutes(df, team_name, num_games, team_id, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()

    ncols = 8
    nrows = df.shape[0]

    ax.set_xlim(0, ncols + 1)
    ax.set_ylim(0, nrows + 1)

    positions = [0.05, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
    columns = ["Player", "Pos", "Age", "MP", "Min", "Mins", "90s"]

    for i in range(nrows):
        for j, column in enumerate(columns):
            fontsize = 10

            if j == 0:
                ha = "left"
            else:
                ha = "center"

            if column == "Mins":
                continue

            text_label = f"{df[column].iloc[i]}"
            weight = "normal"

            if column == "Pos":
                text_label = text_label[:2]

            if column == "Age":
                text_label = text_label[:2]

            if len(text_label) > 17:
                fontsize = 8

            if len(text_label) > 25:
                fontsize = 6

            ax.annotate(
                xy=(positions[j], i + 0.5),
                text=text_label,
                ha=ha,
                va="center",
                weight=weight,
                fontsize=fontsize,
            )

    DC_to_FC = ax.transData.transform
    FC_to_NFC = fig.transFigure.inverted().transform

    DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))

    ax_point_1 = DC_to_NFC([2.25, 0.25])
    ax_point_2 = DC_to_NFC([2.75, 0.75])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([2.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        ax_logo(df["Nation"].iloc[x], flag_ax)

    ax_point_1 = DC_to_NFC([4, 0.05])
    ax_point_2 = DC_to_NFC([5, 0.95])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([7, x + 0.025])
        bar_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        minutes_battery(bar_ax, df["Min"].iloc[x], num_games)

    column_names = [
        "Player",
        "Position",
        "Age",
        "Matches\nPlayed",
        "Mins\nPlayed",
        "% Min.\nPlayed",
        "90s",
    ]

    for index, c in enumerate(column_names):
        if index == 0:
            ha = "left"
        else:
            ha = "center"

        ax.annotate(
            xy=(positions[index], nrows + 0.25),
            text=column_names[index],
            ha=ha,
            va="bottom",
            weight="bold",
        )

    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [nrows, nrows],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )
    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [0, 0],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )

    for x in range(1, nrows):
        ax.plot(
            [ax.get_xlim()[0], ax.get_xlim()[1]],
            [x, x],
            lw=1.15,
            color="gray",
            ls=":",
            zorder=3,
            marker="",
        )

    ax.fill_between(x=[0, 2], y1=nrows, y2=0, color="lightgrey", alpha=0.5, ec="None")

    ax.set_axis_off()

    logo_ax = fig.add_axes([0.825, 0.89, 0.05, 0.05])
    ax_logo(team_id, logo_ax)

    fig.text(
        x=0.15,
        y=0.91,
        s=f"{team_name.replace('-', ' ')} 23/24 {comp_description} ({num_games} Games)",
        ha="left",
        va="bottom",
        weight="bold",
        size=12,
    )

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/minutes/{comp}/{team_name.replace('-', '_').lower()}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_minutes_all(df, lge, comp):
    comp_description = "All Comps"
    if comp != "comps":
        comp_description = LEAGUES.get(comp).get("lge_name")
    lge_id = LEAGUES.get(lge).get("fotmob_id")

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()

    ncols = 8
    nrows = df.shape[0]

    ax.set_xlim(0, ncols + 1)
    ax.set_ylim(0, nrows + 1)

    positions = [0.05, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    columns = ["Player", "Pos", "Age", "MP", "Min", "90s"]

    for i in range(nrows):
        for j, column in enumerate(columns):
            fontsize = 10

            if j == 0:
                ha = "left"
            else:
                ha = "center"

            if column == "Mins":
                continue

            text_label = f"{df[column].iloc[i]}"
            weight = "normal"

            if column == "Pos":
                text_label = text_label[:2]

            if column == "Age":
                text_label = text_label[:2]

            if len(text_label) > 17:
                fontsize = 8

            if len(text_label) > 25:
                fontsize = 6

            ax.annotate(
                xy=(positions[j], i + 0.5),
                text=text_label,
                ha=ha,
                va="center",
                weight=weight,
                fontsize=fontsize,
            )

    DC_to_FC = ax.transData.transform
    FC_to_NFC = fig.transFigure.inverted().transform

    DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))

    ax_point_1 = DC_to_NFC([2.25, 0.25])
    ax_point_2 = DC_to_NFC([2.75, 0.75])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([2.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        ax_logo(df["club_id"].iloc[x], flag_ax)

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([3.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        ax_logo(df["Nation"].iloc[x], flag_ax)

    ax_point_1 = DC_to_NFC([4, 0.05])
    ax_point_2 = DC_to_NFC([5, 0.95])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    column_names = [
        "Player",
        "Position",
        "Age",
        "Matches\nPlayed",
        "Mins\nPlayed",
        "90s",
    ]

    for index, c in enumerate(column_names):
        if index == 0:
            ha = "left"
        else:
            ha = "center"

        ax.annotate(
            xy=(positions[index], nrows + 0.25),
            text=column_names[index],
            ha=ha,
            va="bottom",
            weight="bold",
        )

    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [nrows, nrows],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )
    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [0, 0],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )

    for x in range(1, nrows):
        ax.plot(
            [ax.get_xlim()[0], ax.get_xlim()[1]],
            [x, x],
            lw=1.15,
            color="gray",
            ls=":",
            zorder=3,
            marker="",
        )

    ax.fill_between(x=[0, 2], y1=nrows, y2=0, color="lightgrey", alpha=0.5, ec="None")

    ax.set_axis_off()

    logo_ax = fig.add_axes([0.825, 0.89, 0.05, 0.05])
    ax_logo(lge_id, logo_ax, True)

    fig.text(
        x=0.15,
        y=0.91,
        s=f"Minutes Played 2023/2024 {comp_description}",
        ha="left",
        va="bottom",
        weight="bold",
        size=12,
    )

    annotate_axis(ax)

    save_figure(
        f"figures/{lge}/minutes/{comp}/all_clubs.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_minutes_lges(df, label):
    if label == "comps":
        comp_description = "All Competitons"
    else:
        comp_description = "Leagues Game"

    fig = plt.figure(figsize=(8, 10), dpi=300, facecolor="#EFE9E6")
    ax = plt.subplot()

    ncols = 9
    nrows = df.shape[0]

    ax.set_xlim(0, ncols + 1)
    ax.set_ylim(0, nrows + 1)

    positions = [0.05, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    columns = ["Player", "Pos", "Age", "MP", "Min", "90s"]

    for i in range(nrows):
        for j, column in enumerate(columns):
            fontsize = 10

            if j == 0:
                ha = "left"
            else:
                ha = "center"

            if column == "Mins":
                continue

            text_label = f"{df[column].iloc[i]}"
            weight = "normal"

            if column == "Pos":
                text_label = text_label[:2]

            if column == "Age":
                text_label = text_label[:2]

            if len(text_label) > 15:
                fontsize = 8

            if len(text_label) > 25:
                fontsize = 6

            ax.annotate(
                xy=(positions[j], i + 0.5),
                text=text_label,
                ha=ha,
                va="center",
                weight=weight,
                fontsize=fontsize,
            )

    DC_to_FC = ax.transData.transform
    FC_to_NFC = fig.transFigure.inverted().transform

    DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))

    ax_point_1 = DC_to_NFC([2.25, 0.25])
    ax_point_2 = DC_to_NFC([2.75, 0.75])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([2.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        ax_logo(df["club_id"].iloc[x], flag_ax)

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([3.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        lge_id = LEAGUES.get(df["lge"].iloc[x]).get("fotmob_id")
        ax_logo(lge_id, flag_ax, True)

    for x in range(0, nrows):
        ax_coords = DC_to_NFC([4.25, x + 0.25])
        flag_ax = fig.add_axes([ax_coords[0], ax_coords[1], ax_width, ax_height])
        ax_logo(df["Nation"].iloc[x], flag_ax)

    ax_point_1 = DC_to_NFC([5, 0.05])
    ax_point_2 = DC_to_NFC([6, 0.95])
    ax_width = abs(ax_point_1[0] - ax_point_2[0])
    ax_height = abs(ax_point_1[1] - ax_point_2[1])

    column_names = [
        "Player",
        "Position",
        "Age",
        "Matches\nPlayed",
        "Mins\nPlayed",
        "90s",
    ]

    for index, c in enumerate(column_names):
        if index == 0:
            ha = "left"
        else:
            ha = "center"

        ax.annotate(
            xy=(positions[index], nrows + 0.25),
            text=column_names[index],
            ha=ha,
            va="bottom",
            weight="bold",
        )

    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [nrows, nrows],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )
    ax.plot(
        [ax.get_xlim()[0], ax.get_xlim()[1]],
        [0, 0],
        lw=1.5,
        color="black",
        marker="",
        zorder=4,
    )

    for x in range(1, nrows):
        ax.plot(
            [ax.get_xlim()[0], ax.get_xlim()[1]],
            [x, x],
            lw=1.15,
            color="gray",
            ls=":",
            zorder=3,
            marker="",
        )

    ax.fill_between(
        x=[0, 2.15], y1=nrows, y2=0, color="lightgrey", alpha=0.5, ec="None"
    )

    ax.set_axis_off()

    fig.text(
        x=0.15,
        y=0.91,
        s=f"Europe's Top 5 Leagues 2023/2024 {comp_description}",
        ha="left",
        va="bottom",
        weight="bold",
        size=12,
    )

    annotate_axis(ax)

    save_figure(
        f"figures/combined/minutes/all_minutes_{label}.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
