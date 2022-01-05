import os

# Downloads' output path
# Default: Desktop
# Set this to None to make the output path as current working directory
OUTPUT_PATH = os.path.expanduser('~/Desktop').replace('\\', '/')

# Converts the downloaded audio to .mp3 automatically?
# Default: True
# FFmpeg is required (If this is True)
DOWNLOAD_AUDIO_AS_MP3 = True

# Removes the original audio file after converting it to .mp3 file?
# Default: True
REMOVE_AFTER_CONVERT = True

TITLE_DISPLAY_MAX_LEN = 50

# --------------------------------------------------

# Window's title
TITLE = "YouTube Downloader in Tkinter by ManHinnn0509"

# Window Size, WxH
WINDOW_SIZE = "700x400"

# Allow resize or not
RESIZE_H = False
RESIZE_W = False

# --- Input frame
DEFAULT_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# --- Info frame
THUMBNAIL_PIXELS_X = 107
THUMBNAIL_PIXELS_Y = 80