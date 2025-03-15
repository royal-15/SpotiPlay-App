import re
import shutil
from customtkinter import *
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor

from settings import *
from fileHandle import *
from downloadSpotify import Spotify
from downloadYoutube import Youtube

from titlebar_widgets import titleBar
from inputField_widgets import inputFields
from controlField_widgets import controlField


class App(CTk):
    executor: ThreadPoolExecutor
    spotify: Spotify
    youtube: Youtube

    def __init__(self):
        # Setup
        super().__init__(fg_color=WINDOW_FG)

        # create an executor and spotify and youtube objects
        self.futures = []
        self.executor = ThreadPoolExecutor()
        self.dataWriter = DataWriter("data.txt")
        self.spotify = Spotify(self.executor)
        self.youtube = Youtube(self.executor, futures=self.futures)

        set_appearance_mode("dark")
        self.iconbitmap(WINDOW_LOGO)

        # Window
        self.geometry("600x200")
        self.title("SpotiPlay")
        self.minsize(600, 200)
        self.maxsize(600, 200)

        # Layout
        titleBar(self).pack(side="top", fill="x", pady=(4, 2), padx=4)

        self.inputFields = inputFields(self, onCheck=self.onCheck)
        self.inputFields.pack(side="top", fill="x")

        self.controls = controlField(
            self,
            downloadMethod=self.onDownloadClick,
        )
        self.controls.pack(side="bottom", fill="x")

        # Set Closing Protocol
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # fill the url and path from the file
        url = self.dataWriter.read_url()
        path = self.dataWriter.read_path()
        self.inputFields.input1.getUrlInput().insert(0, url)
        self.inputFields.input2.getPathInput().insert(0, path)

        # Run
        self.mainloop()

    def onCheck(self):
        if self.inputFields.check_var_url.get():
            # write the url to the file
            url = self.inputFields.input1.getUrlInput().get()
            self.dataWriter.write_url(url)

        if self.inputFields.check_var_path.get():
            # write the path to the file
            path = self.inputFields.input2.getPathInput().get()
            self.dataWriter.write_path(path)

    def onDownloadClick(self):
        # Get inputs
        url = self.inputFields.input1.getUrlInput().get()
        path = self.inputFields.input2.getPathInput().get()

        if url == "" or path == "":
            return

        print(f"🔄 Downloading... '{url}'")

        # Check if the URL is a Spotify link
        if self.isSpotifyLink(url):
            # self.spotify.download(url, path)
            future = self.executor.submit(self.spotify.download, url, path)
            self.futures.append(future)
        else:  # It's a YouTube link
            future = self.executor.submit(self.youtube.download, url, path)
            self.futures.append(future)

        self.inputFields.input1.getUrlInput().delete(0, "end")
        self.controls.status.configure(text="🔄 Downloading...")
        self.after(3000, self.checkStatus)

    def isSpotifyLink(self, url: str) -> bool:
        # Returns True if the given URL is a Spotify link, otherwise returns False for YouTube links.
        youtube_patterns = [
            r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/",
        ]

        for pattern in youtube_patterns:
            if re.match(pattern, url):
                return False  # It's a YouTube link

        return True  # It's not a YouTube link

    def on_close(self):
        if messagebox.askyesno("Exit", "Are you sure you want to close?"):
            # Shutdown executor (forcefully stop tasks)
            self.executor.shutdown(wait=False, cancel_futures=True)

            # Destroy the Tkinter window
            self.destroy()
            print("🔴 Application closed.")

    def checkStatus(self):
        # Check if any threads are running & update label accordingly
        active_threads = len(self.executor._threads)

        if active_threads == 0 or all(f.done() for f in self.futures):
            self.controls.status.configure(text="✅ All Done")
        else:
            self.controls.status.configure(text=f"🔄 Downloading...")

        # Check again after 3 second
        self.after(3000, self.checkStatus)


# Check if FFmpeg is installed
# if not shutil.which("ffmpeg"):
#     print("Error: FFmpeg is not installed or not in the system PATH.")
#     print("Please install FFmpeg from https://ffmpeg.org/download.html.")
# else:
#     print("FFmpeg is installed and in the system PATH.")


App()
