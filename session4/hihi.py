import datetime
import pyglet
from datetime import datetime
currentTime = datetime.now().strftime('%H:%M')
print(currentTime)

alarmtime = input("gio bao thuc: ")
while True:
    if alarmtime == currentTime:
        print("Success!!!!")
        music = pyglet.resource.media('crowd-cheering.mp3')
        music.play()

    pyglet.app.run()