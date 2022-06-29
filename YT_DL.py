from pytube import YouTube
from pytube import Playlist
import random
import time

link = 'https://www.youtube.com/watch?v=AehuzeViCG4&list=PLemwF4l2Sz9MwndM2iOMNnafXozxm0P9m'
play_list = Playlist(link)

for cn,video in enumerate(play_list.videos):
    print('starting')
    print(cn, ' ', video.title)
    video.streams.filter(progressive = True, file_extension="mp4").get_by_resolution("720p").download(filename_prefix=str(cn)+' ')
    print('done')
    print('')
    time.sleep(10+random.randrange(1,13)) # waiting between videos downloading
print('all done') # playlist finished
