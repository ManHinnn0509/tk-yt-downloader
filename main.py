import tkinter as tk
from tkinter import *
from pytube import YouTube

from config import *
from widgets.info_frame import InfoFrame
from widgets.input_frame import InputFrame

class YTDL_Window:

    # Don't edit the spaces, it's for padding
    VIDEO_INFO_KEYS = [
        "Title     ",
        "Length",
        "Author",
        "Date    "
    ]

    def __init__(self):
        master = tk.Tk()
        self.master = master

        master.title(TITLE)
        master.geometry(WINDOW_SIZE)
        master.resizable(RESIZE_W, RESIZE_H)

        # Widgets
        self.inputFrame = InputFrame(self, "Video URL: ")
        self.infoFrame = InfoFrame(self, self.VIDEO_INFO_KEYS)

    def exec(self, video, streams):
        
        # Returns string, which means the video cannot be downloaded now
        if (type(video) == str):
            print(video)
            return

        self.infoFrame.update(video)

    def start(self):
        self.master.mainloop()

def main():
    window = YTDL_Window()

    window.start()

if (__name__ == "__main__"):
    main()
