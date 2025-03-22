import yt_dlp


class Youtube:
    def __init__(self, executor, futures, ffmpeg_path):
        self.executor = executor
        self.futures = futures
        self.FFMPEG_PATH = ffmpeg_path

    # playlist check
    def isPlaylist(self, url):
        """Check if the URL is a single video or a playlist using yt-dlp."""
        ydl_opts = {"quiet": True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                url, download=False
            )  # Fetch metadata without downloading

        # 'entries' key exists if it's a playlist (contains multiple videos)
        return "entries" in info

    # youtube songs downloader
    def download(self, url, output_folder):

        import os

        # output folder check
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # playlist check
        if self.isPlaylist(url):
            self.downloadPlaylist(url, output_folder)
        else:
            future = self.executor.submit(self.downloadSong, url, output_folder)
            self.futures.append(future)

    # download playlist
    def downloadPlaylist(self, playlist_url, output_folder):
        # Download all videos mp3 in a playlist using multiple threads.
        ydl_opts = {
            "quiet": True,
            "extract_flat": True,
            "force_generic_extractor": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)

        video_urls = [entry["url"] for entry in info["entries"] if "url" in entry]

        for url in video_urls:
            self.executor.submit(self.downloadSong, url, output_folder)

    # download song
    def downloadSong(self, Song_url, output_folder):
        # yt-dlp options for high-quality MP3 conversion
        ydl_opts = {
            "ffmpeg_location": self.FFMPEG_PATH,
            "format": "bestaudio/best",
            "extractaudio": True,  # Extract only the audio
            "audioformat": "mp3",  # Convert to MP3
            "outtmpl": f"{output_folder}/%(title)s.%(ext)s",  # Save with video title
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",  # High quality 320kbps
                }
            ],
            "keepvideo": False,  # Don't keep the original video file
            "writesubtitles": False,  # Don't download subtitles
            "writeautomaticsub": False,  # Don't download automatic subtitles
            "noplaylist": False,  # Allow playlist downloads
            "quiet": True,  # Reduce output noise
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            song_info = ydl.extract_info(Song_url, download=True)  # Extract metadata
            song_title = song_info.get("title", "Unknown Song")  # Get song title

        print(f"✅ Downloaded Youtube Song: {song_title}")
