import shutil
import customtkinter as ctk
import partials as p

# Check if FFmpeg is installed
if not shutil.which("ffmpeg"):
    print("Error: FFmpeg is not installed or not in the system PATH.")
    print("Please install FFmpeg from https://ffmpeg.org/download.html.")
else:
    print("FFmpeg is installed and in the system PATH.")