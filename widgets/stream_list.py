import os
import threading
import subprocess

import tkinter as tk

from pytubefix import Stream

from config import OUTPUT_PATH, DOWNLOAD_AUDIO_AS_MP3, REMOVE_AFTER_CONVERT

class StreamList:
    def __init__(self, mainWindow, streams, listNameText, buttonText="Download", side="left", isAudio=False) -> None:
        self.mainWindow = mainWindow
        self.master = mainWindow.master

        self.listNameText = listNameText
        self.buttonText = buttonText
        self.side = side

        self.streams = streams
        self.formattedStreams = self.__formatStreams()

        self.isAudio = isAudio

        # Frame that contains everything
        listboxFrame = tk.Frame(self.master)
        self.listboxFrame = listboxFrame

        listName = tk.Label(
            listboxFrame,
            textvariable=tk.StringVar(value=self.listNameText)
        )
        self.listName = listName

        # Listbox that contains the streams
        listbox = tk.Listbox(
            listboxFrame,
            listvariable=tk.StringVar(value=self.formattedStreams),
            width=28
            # fg?
        )
        self.listbox = listbox

        # Scrollbar
        scrollbar = tk.Scrollbar(
            listboxFrame,
            orient='vertical',
            command=listbox.yview
        )
        self.scrollbar = scrollbar

        # Add scrolling to listbox
        self.listbox['yscrollcommand'] = self.scrollbar.set

        button = tk.Button(
            listboxFrame,
            text=self.buttonText,
            command=self.downloadSelection
        )
        self.button = button

        # --- Packing etc.
        
        # Order matters, don't change it
        self.listName.pack()
        self.listbox.pack(fill=tk.Y, expand=True)
        self.button.pack()

        self.listboxFrame.pack(fill=tk.Y, side=self.side, expand=True)
        # self.listboxFrame.pack(fill=tk.Y, side=self.side, expand=True)
    
    def downloadSelection(self):
        # Check if the selection is valid
        try:
            selectedIndex = self.listbox.curselection()[0]
        except IndexError:
            # Maybe the selection is from other listbox
            return

        # Inner function for thread
        def startDownload():
            selectedStream = self.streams[selectedIndex]
            selectedStream: Stream
            
            print(f"--- Current download: {self.formattedStreams[selectedIndex]}")

            outputPath = selectedStream.download(
                output_path=OUTPUT_PATH if (OUTPUT_PATH != None) else "./"
            )

            if not (self.isAudio):
                return

            temp = outputPath.split(".")
            temp.pop(-1)    # Removes the original extension

            mp3OutputPath = ".".join(temp)
            mp3OutputPath = f"{mp3OutputPath}.mp3"

            if (DOWNLOAD_AUDIO_AS_MP3):
                cmdList = [
                    "ffmpeg", "-i",
                    outputPath,
                    "-vn",
                    mp3OutputPath
                ]

                try:
                    subprocess.run(cmdList)
                    print("[SUCCESS] Convert completed!")
                
                    if (REMOVE_AFTER_CONVERT):
                        os.remove(outputPath)
                        
                except:
                    print("[ERROR] Unable to convert downloaded audio file to .mp3")
        
        t = threading.Thread(target=startDownload)
        t.start()

    def update(self, streams):
        self.streams = streams
        self.formattedStreams = self.__formatStreams()

        self.listbox.configure(
            listvariable=tk.StringVar(value=self.formattedStreams)
        )

    def __formatStreams(self):
        l = []
        if (len(self.streams) == 0):
            return l

        for stream in self.streams:
            
            s = ""
            attr = dir(stream)

            # Video with audio
            if ("resolution" in attr and "abr" in attr):
                # Both of them can be in the stream but the value is None
                # So add 2 if to check if it's None or not
                if (stream.resolution != None):
                    s = f"{stream.resolution}"
                
                if (stream.abr != None):
                    if (s == ""):
                        s = f"{stream.abr}"
                    else:
                        s += f" | {stream.abr}"
            
            # Only video
            elif ("resolution" in attr):
                s = f"{stream.resolution}"
            
            # Only audio
            elif ("abr" in attr):
                s = f"{stream.abr}"
            
            # Add itag into it, this is very important
            # s += f" ({stream.itag})"
            s += f" ({stream.mime_type})"

            l.append(s)
        
        return l