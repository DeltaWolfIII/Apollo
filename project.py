from __future__ import unicode_literals
import youtube_dl

URL = input("Enter a song name: ")
URL = URL + " audio"
quality = input("What quality would like your song to be? (low, medium, or high) ")
if quality == 'low':
	bitrate = '96'
if quality == 'medium':
	bitrate = '192'
if quality == 'high':
	bitrate = '320'


print("Downloading song, please wait...")

ytdl_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': bitrate,
    }],
    'default_search': 'auto',
    'quiet': 'on'
}
with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
   ytdl.download([URL])

print("Your song has finished downloading.")
