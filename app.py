import yt_dlp
import os
from yt_dlp.utils import download_range_func

# Commands
# q - Quit
# r - Reset
# f - Download full video

try:
    while 1:
        yt_url = input("Enter a YouTube video URL: ")

        if yt_url == "q":
            break

        video_starts = input("Video starts at (0:0:0): ")

        if video_starts == "q":
            break
        elif video_starts == "r":
            continue

        video_ends = ""

        if video_starts != "f":
            video_ends = input("Video ends at (0:0:0): ")
        else:
            video_starts = "0"
            video_ends = "0"

        if video_ends == "q":
            break
        elif video_ends == "r":
            continue
        elif video_ends == "f":
            video_starts = "0"
            video_ends = "0"

        split_video_start = video_starts.split(":")
        split_video_end = video_ends.split(":")

        hours = 0
        minutes = 0
        seconds = 0

        start_time = 0
        end_time = 0

        for idx, val in enumerate((split_video_start, split_video_end)):
            if len(val) == 3:
                hours = int(val[0]) * 60 * 60
                minutes = int(val[1]) * 60
                seconds = int(val[2])
            elif len(val) == 2:
                minutes = int(val[0]) * 60
                seconds = int(val[1])
            else:
                seconds = int(val[0])

            if idx == 0:
                start_time = hours + minutes + seconds
            else:
                end_time = hours + minutes + seconds


        ydl_opts = {
            "format": "mp4",
            # "format": "bestvideo+bestaudio/best",
            "ffmpeg_location": f"{os.getenv('USERPROFILE')}/Desktop/YT-DL/bin",
            "download_ranges": download_range_func(None, [(start_time, end_time)]),
            "force_keyframes_at_cuts": True,
            "overwrites": True,
            "outtmpl": f"{os.getenv('USERPROFILE')}/Downloads/%(title)s.%(ext)s"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(yt_url)

except Exception as e:
    print(e)
