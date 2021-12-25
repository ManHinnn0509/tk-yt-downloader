import tkinter as tk

from config import DEFAULT_URL
from util.yt_utils import getVideo

# Copied and edited from:
# https://github.com/ManHinnn0509/SAR-Stats-Helper/blob/1b76e4ff140ce3241c9f3ff29273faaf5ff519a1/widgets/input_frame.py#L5

class InputFrame:
    def __init__(self, mainWindow, inputLabelText="Input here", row=0) -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master
        self.inputLabelText = inputLabelText
        self.row = row

        inputFrame = tk.Frame(self.master)

        # Label
        self.inputLB = tk.Label(inputFrame, text=self.inputLabelText)
        self.inputLB.grid(row=self.row, column=0)

        # Input
        self.inputEntry = tk.Entry(inputFrame, width=40)
        self.inputEntry.insert(0, DEFAULT_URL)
        self.inputEntry.bind('<Return>', lambda event: self.__press())   # The lambda is for ignoring the "event" object
        self.inputEntry.grid(row=self.row, column=1)

        # Submit button
        self.inputButton = tk.Button(inputFrame, text="Submit", command=self.__press)
        self.inputButton.grid(row=self.row, column=2)

        self.inputFrame = inputFrame
        self.inputFrame.pack()
    
    def __press(self):
        # Get the input string from entry, should be video URL
        s = self.inputEntry.get()
        if (s == ""):
            return

        v, streams = getVideo(s)
        
        self.mainWindow.exec(s, streams)