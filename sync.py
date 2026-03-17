import yt_dlp

def run_sync():
    ydl_opts = {
    'format': 'bestaudio/best',
    'download_archive': 'archive.txt',
    'outtmpl': 'music/raw/%(title)s.%(ext)s',
    # ADD THESE TWO LINES:
    'noplaylist': True,       # If you pass a link with '&list=', it only takes the video
    'ignoreerrors': True,     # Keeps going if one song fails
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {'key': 'FFmpegMetadata'}, {'key': 'EmbedThumbnail'}],
}
    
    # You can paste your 700 links here or a single Playlist URL
    urls = [
        'https://www.youtube.com/watch?v=vZpVgetTSKs&list=RD7SACxTvWI8I&index=14'
    ]
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    run_sync()