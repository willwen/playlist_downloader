from __future__ import unicode_literals
import youtube_dl
# did you save your code in file youtube_search_dl.py ? if yes then import loads your file instead expected module
import re


class MyLogger(object):
    def debug(self, msg):
        print("[Debug]: {}".format(msg))
        pass

    def warning(self, msg):
        print("[Warning]:\t{}".format(msg))
        pass

    def error(self, msg):
        print("[Error]:\n{}".format(msg))


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download_webfile(url, filename=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'default_search': 'ytsearch1',
    }
    if filename is not None:
        ydl_opts["outtmpl"] = filename
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


with open("batch3.txt") as f:
    lines = f.readlines()
    for line in lines:
        # remove_newline
        search_term = line.replace(":", " - ").rstrip()

        filename = re.sub(r"(\\|\/|\:|\*|\"|<|>|\||\.)", " ", search_term) + ".mp4"
        download_webfile(search_term, filename)
