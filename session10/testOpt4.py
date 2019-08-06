# from youtube_dl import YoutubeDL
from __future__ import unicode_literals
import json
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

# ydl_opts = {
#     'default-search': 'ytsearch3'
# }

with open('data.json') as outFile:
    data = json.load(outFile)

songSearch = input("Name Song Search: ")

optionsExtract = {
    'default_search': 'ytsearch3',
}

ydl = youtube_dl.YoutubeDL(optionsExtract)
ydlNew = youtube_dl.YoutubeDL(ydl_opts)

search_result = ydl.extract_info(songSearch, download = False)
for i in range(len(search_result['entries'])):
    print(i + 1, search_result['entries'][i]['title'])

indexSongDownload = int(input("Song you want to download ? ")) - 1
print(search_result['entries'][indexSongDownload]['webpage_url'])

songDownload = ydlNew.extract_info(search_result['entries'][indexSongDownload]['id'], download=True)

data.append(songDownload)

with open('data.json', 'w') as f:
    json.dump(data, f)
