import os

# Window's title
TITLE = "YouTube Downloader in Tkinter by ManHinnn0509"

# Window Size, WxH
WINDOW_SIZE = "700x400"

# Downloads' output path
# Set this to None to make the output path as current working directory
OUTPUT_PATH = os.path.expanduser('~/Desktop').replace('\\', '/')

# Allow resize or not
RESIZE_H = False
RESIZE_W = False

# --- Input frame
DEFAULT_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# --- Info frame
THUMBNAIL_PIXELS_X = 107
THUMBNAIL_PIXELS_Y = 80

TITLE_DISPLAY_MAX_LEN = 50