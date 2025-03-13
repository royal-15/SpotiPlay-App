import os
import subprocess


def download_spotify_playlist(playlist_url, download_folder):
    # Ensure the output directory exists
    os.makedirs(download_folder, exist_ok=True)

    print(f"Starting download... Songs will be saved in: {download_folder}")

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
