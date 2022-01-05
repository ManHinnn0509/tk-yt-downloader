# tk-yt-downloader

A YouTube downloader in Tkinter

P.S: The GUI may not look good since I don't really have a good art sense. Sorry!

## How to use?

1) Paste the video url into the input field on the top of the window
2) Press the "Submit" button
3) Wait for the program to load
4) Click to select the stream you want to download
5) Press the "Download" button under the listbox

## Requirements

See [requirements.txt](./requirements.txt)

Also, [FFmpeg](https://github.com/FFmpeg/FFmpeg) is needed for **merging video & audio parts** / **audio download converting**

## Config

There are some options that are configurable, see [config.py](./config.py) for more details

## Merging / Converting

### Merging the download parts (Video & audio)

You can merge them by the following command (From [here](https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg)):

```
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```

Change `video.mp4`, `audio.wav`, and also `output.mp4` to your file names

### Converting .webm to .mp3

You can convert `.webm` file to `.mp3` file with the following command (Edited from [here](https://stackoverflow.com/questions/44926858/batch-script-to-convert-youtube-dl-webm-file-to-mp3-with-ffmpeg))

```
ffmpeg -i input.webm -vn -ab 128k -ar 44100 -y output.mp3
```

Or:

```
ffmpeg -i input.webm -vn output.mp3
```

Change `input.webm` and `output.mp3` to your file names

## Demo

* Launch up

![](./img/example/example_default.png)

* Result

![](./img/example/example_result.png)

![](./img/example/example_result_2.png)

## Planned

* [ ] Best quality stream download button
    * [ ] Video
    * [ ] Audio
* [ ] Merge button (Merge video & audio)
* [ ] Create `.exe` builds
* [x] ~~Convert button~~ [Convert audio download automatically](https://github.com/ManHinnn0509/tk-yt-downloader/commit/076012497d3bbd206b166bb5dbce3cdcd152921b)
* [x] [Optional output path](https://github.com/ManHinnn0509/tk-yt-downloader/commit/69ecfc142d82d5ada2cc9429a0a1624b992b4ed8)
* [x] [Maximum title display length](https://github.com/ManHinnn0509/tk-yt-downloader/commit/b9ca71bd3ba68379bfba92f49a93a23b6f8b6605)
* [x] [Sort streams by it's quality (Highest to lowest)](https://github.com/ManHinnn0509/tk-yt-downloader/commit/b9ca71bd3ba68379bfba92f49a93a23b6f8b6605)

## Disclaimer

This program should only be used on **non-copyrighted** material.

