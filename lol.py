ytdl_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'default_search': 'auto',
    'quiet': 'on'
}
with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
   ytdl.download([url]
