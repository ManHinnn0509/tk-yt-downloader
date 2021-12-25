import tkinter as tk
from tkinter import *
from pytube import YouTube

from config import *
from widgets import *

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

        # Listbox(es) for streams
        self.videoWithAudioListbox = StreamList(self, [], "Video with audio", "Download", "left")
        self.onlyVideoListbox = StreamList(self, [], "Video only", "Download", "left")
        self.onlyAudioListbox = StreamList(self, [], "Audio only", "Download", "left")

    def exec(self, video, streams):
        
        # Returns string, which means the video cannot be downloaded now
        if (type(video) == str):
            print(video)
            return

        # Update the video's info
        self.infoFrame.update(video)

        # Update stream lists
        onlyAudio = streams.filter(only_audio=True)
        onlyVideo = streams.filter(only_video=True)
        videoWithAudio = (set(streams) - set(onlyVideo)) - set(onlyAudio)

        videoWithAudio = list(videoWithAudio)
        onlyAudio = list(onlyAudio)
        onlyVideo = list(onlyVideo)

        self.videoWithAudioListbox.update(videoWithAudio)
        self.onlyVideoListbox.update(onlyVideo)
        self.onlyAudioListbox.update(onlyAudio)

    def start(self):
        self.master.mainloop()

def main():
    window = YTDL_Window()

    window.start()

if (__name__ == "__main__"):
    main()
