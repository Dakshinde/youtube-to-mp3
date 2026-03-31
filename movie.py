import yt_dlp

def download_best_quality(url):
    ydl_opts = {
        # 'bestvideo+bestaudio/best' ensures it grabs the highest resolution
        'format': 'bestvideo+bestaudio/best',
        # Merges video and audio into an mp4 container
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading: {url}")
        ydl.download([url])

video_url = "https://www.youtube.com/shorts/8IrLkEmuUHk"
download_best_quality(video_url)