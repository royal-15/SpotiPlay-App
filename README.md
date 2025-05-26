# SpotiPlay

A modern, user-friendly desktop application for downloading music from Spotify and YouTube. Built with Python and CustomTkinter, SpotiPlay offers a sleek interface and seamless download experience.

![SpotiPlay Logo](resources/logo1.ico)

## Features

-   🎵 Download music from both Spotify and YouTube
-   🎨 Modern, dark-themed user interface
-   💾 Automatic saving of download location and last used URL
-   🔄 Background download processing
-   ⚡ Fast and efficient downloads
-   🎯 Support for both Spotify and YouTube links
-   🔍 Automatic link detection
-   📁 Custom download directory selection

## Installation

### Prerequisites

-   Windows 10 or later
-   Python 3.7 or later (for development)

### Quick Download

1. Go to the [Installers](dist/installers) folder
2. Download the latest version (e.g., `SpotiPlay-v1.0.0.zip`)
3. Extract the zip file to your desired location
4. Run `SpotiPlay.exe`

### Running from Source

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SpotiPlay-App.git
cd SpotiPlay-App
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python SpotiPlay.py
```

## Usage

1. Launch SpotiPlay
2. Enter a Spotify or YouTube URL in the URL field
3. Select your desired download location
4. Click the download button
5. Wait for the download to complete
6. Enjoy listening you Favorite Songs

### Features in Detail

#### URL Input

-   Supports both Spotify and YouTube links
-   Automatically detects the type of link
-   Saves the last used URL for convenience

#### Download Location

-   Choose any directory on your computer
-   Location is remembered between sessions
-   Creates necessary folders automatically

#### Download Status

-   Real-time status updates
-   Progress indication
-   Error handling and retry options

## Development

### Project Structure

```
SpotiPlay-App/
├── modules/
│   ├── fileHandle.py
│   ├── settings.py
│   ├── titlebar_widgets.py
│   ├── inputField_widgets.py
│   ├── controlField_widgets.py
│   ├── downloadSpotify.py
│   └── downloadYoutube.py
├── resources/
│   └── logo1.ico
├── SpotiPlay.py
├── ffmpeg.exe
└── requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

-   [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI components
-   [spotdl](https://github.com/spotDL/spotify-downloader) for Spotify download functionality
-   [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube download functionality
