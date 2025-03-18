import os
import sys
import subprocess
from mutagen.mp3 import MP3
from concurrent.futures import ThreadPoolExecutor


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
                creationflags=(
                    subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
                ),
            )
            print(f"✅ Downloaded: {url} in {download_folder}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to download: {self.getSongName(url)}")
            print(f"Error message:\n{e.stderr}")

    def isFileIncomplete(self, file_path):
        # Check if an MP3 file is incomplete by verifying its metadata.
        try:
            audio = MP3(file_path)  # Load metadata
            if (
                audio.info.length < 30
            ):  # Example: Songs shorter than 30 sec are considered incomplete
                return True
        except Exception:  # If MP3 metadata can't be read, assume it's corrupted
            return True
        return False

    def retryDownloads(self, path):
        # Retry downloading incomplete MP3 files in the folder.
        print("🔍 Checking for incomplete downloads...")

        for file_name in os.listdir(path):
            if file_name.endswith(".mp3"):
                file_path = os.path.join(path, file_name)

                # Check if the file is incomplete
                if self.isFileIncomplete(file_path):
                    print(
                        f"⚠️ Incomplete file detected: {file_name} — Retrying download..."
                    )

                    # Extract song name (assuming it's in the filename)
                    song_name = os.path.splitext(file_name)[0]

                    try:
                        # Re-download using spotdl
                        subprocess.run(
                            [
                                "spotdl",
                                "download",
                                song_name,
                                "--output",
                                path,
                            ],
                            check=True,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            creationflags=(
                                subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
                            ),
                        )
                        print(f"✅ Successfully re-downloaded: {file_name}")
                    except subprocess.CalledProcessError:
                        print(f"❌ Failed to re-download: {file_name}")
