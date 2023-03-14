import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from utils import ax_logo, nation_colours, save_figure, remove_plot_border


def annotate_axis(ax):
    ax.annotate(
        "Stats from fbref.com",
        (0, 0),
        (0, -40),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    ax.annotate(
        "Data Viz by @plvizstats || u/plvizstats",
        (0, 0),
        (0, -50),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    return ax


def plt_nationalities(df_players, df_times, df_sum, competition, comp_title, fotmob_id):
    fig = plt.figure(figsize=(20, 10), facecolor="#EFE9E6")
    fig.subplots_adjust(hspace=0.5)
    gs = GridSpec(nrows=3, ncols=1)
    fig.suptitle(f"{comp_title} Nationalities", fontsize=22)

    ax0 = fig.add_subplot(gs[0, 0])
    bars = ax0.bar(
        df_players["Nation"],
        df_players["# Players"],
        color=nation_colours(df_players["Nation"]),
    )
    ax0.bar_label(bars, size=16)
    ax0.set_title("Number of players from each nation (Top 10)", size=20)
    ax0.set_xlabel("Nations", size=16)
    ax0.set_ylabel("# of Players", size=16)
    ax0.set_facecolor("#EFE9E6")
    remove_plot_border(ax0)
    for label in ax0.get_xticklabels() + ax0.get_yticklabels():
        label.set_fontsize(14)

    ax1 = fig.add_subplot(gs[1, 0])
    bars = ax1.bar(
        df_times["Nation"], df_times["Min"], color=nation_colours(df_times["Nation"])
    )
    ax1.bar_label(bars, size=16)
    ax1.set_title("Number of minutes played by nation (Top 10)", size=20)
    ax1.set_xlabel("Nations", size=16)
    ax1.set_ylabel("Minutes", size=16)
    ax1.set_facecolor("#EFE9E6")
    remove_plot_border(ax1)
    for label in ax1.get_xticklabels() + ax1.get_yticklabels():
        label.set_fontsize(14)

    ax2 = fig.add_subplot(gs[2, 0])
    bars = ax2.bar(
        df_sum["Nation"], df_sum["Goals"], color=nation_colours(df_sum["Nation"])
    )
    ax2.bar_label(bars, size=16)
    ax2.set_title("Number of goals scored from each nation (Top 10)", size=20)
    ax2.set_xlabel("Nations", size=16)
    ax2.set_ylabel("Goals", size=16)
    ax2.set_facecolor("#EFE9E6")
    remove_plot_border(ax2)
    for label in ax2.get_xticklabels() + ax2.get_yticklabels():
        label.set_fontsize(14)

    annotate_axis(ax2)

    logo_ax = fig.add_axes([0.125, 0.88, 0.08, 0.08])
    ax_logo(fotmob_id, logo_ax, True)

    save_figure(
        f"figures/nationalities/{competition}-nations.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()


def plt_nationalities_combined(df_total_players, df_total_times, df_total_goals):
    fig = plt.figure(figsize=(20, 10), facecolor="#EFE9E6")
    fig.subplots_adjust(hspace=0.5)
    gs = GridSpec(nrows=3, ncols=1)
    fig.suptitle(f"Top 5 Leagues Nationalities", fontsize=22)

    ax0 = fig.add_subplot(gs[0, 0])
    bars = ax0.bar(
        df_total_players["Nation"],
        df_total_players["# Players"],
        color=nation_colours(df_total_players["Nation"]),
    )
    ax0.bar_label(bars, size=16)
    ax0.set_title("Number of players from each nation (Top 10)", size=20)
    ax0.set_xlabel("Nations", size=16)
    ax0.set_ylabel("# of Players", size=16)
    ax0.set_facecolor("#EFE9E6")
    remove_plot_border(ax0)
    for label in ax0.get_xticklabels() + ax0.get_yticklabels():
        label.set_fontsize(14)

    ax1 = fig.add_subplot(gs[1, 0])
    bars = ax1.bar(
        df_total_times["Nation"],
        df_total_times["Min"],
        color=nation_colours(df_total_times["Nation"]),
    )
    ax1.bar_label(bars, size=16)
    ax1.set_title("Minutes played from each nation (Top 10)", size=20)
    ax1.set_xlabel("Nations", size=16)
    ax1.set_ylabel("Minutes", size=16)
    ax1.set_facecolor("#EFE9E6")
    remove_plot_border(ax1)
    for label in ax1.get_xticklabels() + ax1.get_yticklabels():
        label.set_fontsize(14)

    ax2 = fig.add_subplot(gs[2, 0])
    bars = ax2.bar(
        df_total_goals["Nation"],
        df_total_goals["Goals"],
        color=nation_colours(df_total_goals["Nation"]),
    )
    ax2.bar_label(bars, size=16)
    ax2.set_title("Goals scored from each nation (Top 10)", size=20)
    ax2.set_xlabel("Nations", size=16)
    ax2.set_ylabel("Goals", size=16)
    ax2.set_facecolor("#EFE9E6")
    remove_plot_border(ax2)
    for label in ax2.get_xticklabels() + ax2.get_yticklabels():
        label.set_fontsize(14)

    annotate_axis(ax2)

    save_figure(
        f"figures/nationalities/top_five_leagues_combined.png",
        300,
        False,
        "#EFE9E6",
        "tight",
    )

    plt.close()
