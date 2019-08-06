from __future__ import unicode_literals
import json
import pyglet
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load
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

while True:
    print("This is blabla music app")
    print("Pick one of the options : ")

    print('''
    1.Show all songs
    2.Show details of a song
    3.Play a song
    4.Search and dl a song
    5.Exit
    ''')

    ans = int(input(">>>"))
    if ans == 2:
        print("Song list is empty")
        input("Press Enter to continue...")

    elif ans == 3:
        print("Song list is empty")
        input("Press Enter to continue...")

    elif ans == 5:
        break
    elif ans == 1:
        print("Song list is empty")
        input("Press Enter to continue...")

    else:
        with open('data.json') as outFile:
            data = json.load(outFile)
            
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

        songSearch = input("Name Song Search: ")

        optionsExtract = {
            'quiet': True,
            'no_warnings': True,
            'default_search': 'ytsearch3',
        }

        ydl = youtube_dl.YoutubeDL(optionsExtract)
        ydlNew = youtube_dl.YoutubeDL(ydl_opts)

        search_result = ydl.extract_info(songSearch, download = False)
        for i in range(len(search_result['entries'])):
            print(i + 1, search_result['entries'][i]['title'])

        indexSongDownload = int(input("Song you want to download ? ")) - 1
        # print(search_result['entries'][indexSongDownload]['webpage_url'])

        songDownload = ydlNew.extract_info(search_result['entries'][indexSongDownload]['webpage_url'], download=True)

        data.append(songDownload)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        mp3File = data[indexSongDownload]['title']+".mp3"        
        player = Player()
        source = load(mp3File)
        player.queue(source)
        player.play()
        # while True:
        # out_put = input('play , pause or stop ?').lower()
        # if out_put == 'play':
        #     player.play()
        # elif out_put == 'pause':
        #     player.pause()
        # elif out_put == "stop":
        #     player.pause()
        #     break





