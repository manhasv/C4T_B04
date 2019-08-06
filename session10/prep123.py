from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'outtmpl': '%(id)s', # lấy tên file đown về là id của video
    'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

# from youtube_dl import YoutubeDL
# import json
# ydl_opts = {
#     'default-search': 'ytsearch3'
# }
# # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
# #     result = ydl.extratc_info(['https://www.youtube.com/watch?v=BaW_jenozKc'], download=False)
# lis =[]
# ydl = YoutubeDL(ydl_opts)
# result = ydl.extract_info('https://www.youtube.com/watch?v=Wv2rLZmbPMA', download=False)
# re = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
# lis.append(re)
# lis.append(result)

# print(lis)
# with open('data.json', 'w') as f:
#     json.dump(lis, f)

