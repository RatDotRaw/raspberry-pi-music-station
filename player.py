import os
import time
import random

path = "/home/pi/Desktop/pimusic/music"

os.chdir(path)

while True:
    musicList = os.listdir(path)
    random.shuffle(musicList)

    for music in musicList:
        os.system('espeak -s 150 "now playing: ' + music.split(".", 1)[0] + '"')
        os.system('ffplay -nodisp -autoexit "' + music + '"')
        time.sleep(10)
