import tkinter as tk

from util.utils import genLabelText
from util.img_utils import readImgFromPath
from config import THUMBNAIL_PIXELS_X, THUMBNAIL_PIXELS_Y

# Video info

class InfoFrame:

    def __init__(self, mainWindow, infoKeys) -> None:
        self.mainWindow = mainWindow
        self.master = mainWindow.master

        self.infoKeys = infoKeys

        # Create the frame
        infoFrame = tk.Frame(self.master)

        # Default video thumbnail
        self.thumbnail = readImgFromPath(
            "./img/default.png", 
            THUMBNAIL_PIXELS_X, THUMBNAIL_PIXELS_Y
        )

        # Default video info
        defaultValue = "-"
        infoMsg = tk.Label(
            infoFrame,
            justify=tk.LEFT,
            compound="left",
            image=self.thumbnail,
            text=genLabelText(
                [f"{k} : {defaultValue}" for k in self.infoKeys], " "
            )
        )

        self.infoMsg = infoMsg
        self.infoFrame = infoFrame

        # Grid, pack etc.
        self.infoMsg.grid(row=1, column=0)
        self.infoFrame.pack()
    
    def update(self, video, streams):
        pass
