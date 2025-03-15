import subprocess
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor


load_dotenv()


class Spotify:
    def __init__(self, executor: ThreadPoolExecutor):
        self.executor = executor

    def download(self, url, download_folder):
        try:
            result = subprocess.run(
                [
                    "spotdl",
                    "download",
                    url,
                    "--output",
                    download_folder,
                    "--format",
                    "mp3",
                    "--bitrate",
                    "320k",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            print(f"✅ Downloaded: {url} in {download_folder}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to download: {self.getSongName(url)}")
            print(f"Error message:\n{e.stderr}")
