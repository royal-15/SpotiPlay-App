import os
import subprocess
import shutil
import threading
from customtkinter import *
from partials import *
from settings import *

from titlebar_widgets import titleBar
from inputField_widgets import inputFields
from controlField_widgets import controlField


class App(CTk):
    def __init__(self):
        # Setup
        super().__init__(fg_color=WINDOW_FG)
        set_appearance_mode("dark")
        self.iconbitmap(WINDOW_LOGO)

        self.geometry("600x200")
        self.title("SpotiPlay")
        self.minsize(600, 200)
        self.maxsize(600, 200)

        titleBar(self).pack(side="top", fill="x", pady=(4, 2), padx=4)

        self.inputFields = inputFields(self)
        self.inputFields.pack(side="top", fill="x")

        controlField(
            self,
            downloadMethod=self.onDownloadClick,
            resetMethod=self.onResetClick,
        ).pack(side="bottom", fill="x")

        # Run
        self.mainloop()

    def onDownloadClick(self):
        url = self.inputFields.input1.getUrlInput().get()
        path = self.inputFields.input2.getPathInput().get()
        print(f"downloading... '{url}' in '{path}'")
        thread = threading.Thread(target=self.download, args=(url, path))
        thread.start()
        self.inputFields.input1.getUrlInput().delete(0, "end")

    def onResetClick(self):
        print("reset button clicked")

    # songs downloader
    def download(self, playlist_url, download_folder):
        # Ensure the output directory exists
        os.makedirs(download_folder, exist_ok=True)

        # Run the spotdl command to download the playlist with high-quality settings
        try:
            result = subprocess.run(
                [
                    "spotdl",
                    "download",
                    playlist_url,
                    "--output",
                    download_folder,
                    "--format",
                    "mp3",  # Choose format
                    "--bitrate",
                    "320k",  # Set audio quality
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            print("Download completed successfully!")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("An error occurred while downloading the playlist.")
            print(
                "Probably the 'spotdl' library is missing (Run 'pip install spotdl' to install it.)"
            )
            print(f"Error message:\n{e.stderr}")


# Check if FFmpeg is installed
# if not shutil.which("ffmpeg"):
#     print("Error: FFmpeg is not installed or not in the system PATH.")
#     print("Please install FFmpeg from https://ffmpeg.org/download.html.")
# else:
#     print("FFmpeg is installed and in the system PATH.")


App()
