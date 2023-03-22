import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image

from constants import AGGREGATOR, NINETY_COLUMNS


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


def ax_logo(logo_id, ax, league=False):
    url = "https://images.fotmob.com/image_resources/logo/teamlogo/"
    if league:
        url = "https://images.fotmob.com/image_resources/logo/leaguelogo/"
    icon = Image.open(urllib.request.urlopen(f"{url}{logo_id}.png"))
    ax.imshow(icon)
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


def nation_colours(col):
    primary_colour = {
        "Argentina": "#43A1D5",
        "Nigeria": "#008751",
        "Denmark": "#C60C30",
        "Germany": "#000000",
        "Belgium": "#E30613",
        "France": "#21304D",
        "Portugal": "#E42518",
        "Norway": "#C8102E",
        "Brazil": "#FFDC02",
        "England": "#000040",
        "Spain": "#8B0D11",
        "Poland": "#DC143C",
        "Italy": "#0064AA",
        "Chile": "#0039A6",
        "Senegal": "#11A335",
        "Morocco": "#17A376",
        "Algeria": "#007229",
        "Canada": "#C5281C",
        "Suriname": "#377E3F",
        "Japan": "#000555",
        "Austria": "#ED2939",
        "Netherlands": "#F36C21",
        "Israel": "#0038B8",
        "Serbia": "#B72E3E",
        "Croatia": "#ED1C24",
        "Uruguay": "#55B5E5",
        "Republic of Ireland": "#169B62",
        "Wales": "#AE2630",
        "Scotland": "#004B84",
        "Colombia": "#FCD116",
        "Kosovo": "#244AA5",
        "Czech Republic": "#ED1B2C",
        "Switzerland": "#D52B1E",
        "Albania": "#E41E20",
        "Côte d'Ivoire": "#FF8200",
        "Mali": "#FCD116",
        "Cameroon": "#479A50",
        "Ghana": "#D40023",
        "Bosnia": "#002F6C",
        "Ukraine": "#FFD700",
        "Cameroon": "#479A50",
        "Turkey": "#E30A17",
        "Switzerland": "#FF0000",
        "Egypt": "#C8102E",
        "United States": "#002868",
        "Angola": "#C8102E",
    }

    clr = []
    for team in col:
        if team in primary_colour:
            clr.append(primary_colour[team])
        else:
            print(team)
    return clr


def dict_conversion(country):
    countries = {
        "ar ARG": "Argentina",
        "ng NGA": "Nigeria",
        "dk DEN": "Denmark",
        "de GER": "Germany",
        "be BEL": "Belgium",
        "fr FRA": "France",
        "pt POR": "Portugal",
        "no NOR": "Norway",
        "br BRA": "Brazil",
        "eng ENG": "England",
        "es ESP": "Spain",
        "pl POL": "Poland",
        "it ITA": "Italy",
        "cl CHI": "Chile",
        "sn SEN": "Senegal",
        "ma MAR": "Morocco",
        "dz ALG": "Algeria",
        "ca CAN": "Canada",
        "sr SUR": "Suriname",
        "jp JPN": "Japan",
        "at AUT": "Austria",
        "nl NED": "Netherlands",
        "il ISR": "Israel",
        "rs SRB": "Serbia",
        "hr CRO": "Croatia",
        "uy URU": "Uruguay",
        "xk KVX": "Kosovo",
        "ua UKR": "Ukraine",
        "gh GHA": "Ghana",
        "ba BIH": "Bosnia",
        "cm CMR": "Cameroon",
        "ch SUI": "Switzerland",
        "eg EGY": "Egypt",
        "tr TUR": "Turkey",
        "ao ANG": "Angola",
    }
    return countries.get(country)
