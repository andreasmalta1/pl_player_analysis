import bar_chart_race as bcr
import urllib.request
from PIL import Image
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import subprocess

from constants import LEAGUES


def get_video(df, competition_name, lge, year):
    bcr.bar_chart_race(
        df=df,
        n_bars=15,
        sort="desc",
        title=f"{competition_name} Clubs Points Since {year}",
        filename=f"videos/{lge}_clubs.mp4",
        filter_column_colors=True,
        period_length=700,
        steps_per_period=30,
        dpi=300,
        cmap="pastel1",
    )


def freeze_video(lge):
    subprocess.call(
        'ffmpeg -i %s -vf tpad=stop_mode=clone:stop_duration=2, -vf "setpts=1.75*PTS", %s'
        % (f"videos/{lge}_clubs.mp4", f"videos/{lge}_clubs_long.mp4"),
        shell=True,
    )

    # video = VideoFileClip(f"videos/{lge}_clubs_long.mp4").fx(
    #     vfx.freeze, t="end", freeze_duration=3
    # )

    # if lge != "combined":
    #     league_id = LEAGUES[lge].get("fotmob_id")
    #     url = "https://images.fotmob.com/image_resources/logo/leaguelogo/"
    #     icon = Image.open(urllib.request.urlopen(f"{url}{league_id}.png"))

    #     logo = (
    #         ImageClip(icon)
    #         .with_duration(video.duration)
    #         .resize(height=95)
    #         .margin(right=8, top=8, opacity=0)
    #         .with_position(("right", "top"))
    #     )

    # footer_one = (
    #     TextClip("Stats from fbref.com", font_size=25, color="black")
    #     .with_position((334, video.h - 75))
    #     .with_duration(video.duration)
    #     .with_start(0)
    # )

    # footer_two = (
    #     TextClip(
    #         "Data Viz by Andreas Calleja @andreascalleja", font_size=25, color="black"
    #     )
    #     .with_position((330, video.h - 40))
    #     .with_duration(video.duration)
    #     .with_start(0)
    # )

    # final = CompositeVideoClip([video, logo or None, footer_one, footer_two])
    # final.write_videofile(f"videos/{lge}_clubs_draft.mp4", codec="libx264")
    # ffmpeg_extract_subclip(
    #     f"videos/{lge}_clubs_draft.mp4",
    #     0,
    #     (final.duration - 3),
    #     f"videos/final/{lge}_clubs.mp4",
    # )
