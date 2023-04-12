from pytube import YouTube
from sys import argv
import os

try:
    link = argv[1]
except IndexError:
    link = input('Please type the video url\n')
op = input('Do you want download a video or only audio?\n')
yt = YouTube(link)

print('Title: {}'.format(yt.title))

print('Views: {}'.format(yt.views))

if 'v' in op.lower():
    yd = yt.streams.get_highest_resolution()
else:
    yd = yt.streams.filter(only_audio=True).first()
    
file = yd.download('./downloads')

if 'v' not in op.lower():
    base, ext = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
     
print(yt.title + " has been successfully downloaded.")