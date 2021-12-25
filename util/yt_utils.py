"""
    Util file extracted from Cyberpsycho.py
    Date: 25/12/2021
"""

import re
from typing import Union

from pytube import YouTube, Playlist
from pytube.streams import Stream
from pytube.exceptions import AgeRestrictedError, RegexMatchError, VideoUnavailable

from urllib.error import URLError

def __intExtract(s: str):
    # return int(re.sub("[^0-9]", "", s))
    return int(re.sub("\D", "", s))

def streamsFilter(video: YouTube, audioOnly=True) -> Union[list, None]:
    """
        Returns a list of AUDIO streams if audioOnly=True \n
        Returns a list of VIDEO streams if audioOnly=False \n
        None will be returned if Exception caught.
    """
    try:
        streams = video.streams
        audioStreams = streams.filter(only_audio=True)
        if (audioOnly):
            return list(audioStreams)
        else:
            videoStreams = set(streams) - set(audioStreams)
            return list(videoStreams)
    except:
        return None

def getBestVideoStreamWithAudio(video: YouTube) -> Union[Stream, None]:
    """
        Returns the best quality stream of video WITH audio
    """

    streams = video.streams
    audioStreams = video.streams.filter(only_audio=True)
    videoStreams = video.streams.filter(only_video=True)
    
    vs = set(streams) - set(audioStreams) - set(videoStreams)

    best = -1
    bestStream = None
    for s in vs:
        res = __intExtract(s.resolution)
        if (res > best):
            best = res
            bestStream = s

    return bestStream

def getMaxResolutionStream(video: YouTube) -> Union[Stream, None]:
    """
        Returns the best quality stream of the video.
        None will be returned when no match found.
    """
    # This is actually a Json and we can know what's the maximum resolution of the video via it
    # maxResolution = video.vid_info["playerConfig"]["decodeQualityConfig"]["maximumVideoDecodeVerticalResolution"]

    try:
        # Filter out video streams only
        streams = video.streams
        videoStreams = set(streams) - set(streams.filter(only_audio=True))

        best = -1
        bestStream = None

        # Returns the correct stream
        for s in videoStreams:
            res = __intExtract(s.resolution)
            if (res > best):
                best = res
                bestStream = s
        
        return bestStream
    except Exception as e:
        return None

def getMaxQualityAudioStream(video: YouTube) -> Union[Stream, None]:
    """
        Returns the best quality audio stream.
        None will be returned if nothing were found.
    """
    try:
        audioStreams = video.streams.filter(only_audio=True)

        bestStream = None
        best = -1
        # Find the best quality audio stream
        for s in audioStreams:
            # Convert the abr (quality) into int using regex
            # See: https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python
            quality = __intExtract(s.abr)
            if (quality > best):
                best = quality
                bestStream = s
        
        return bestStream
    except Exception as e:
        return None

def loadPlaylist(url) -> Union[Playlist, None]:
    """
        A pytube.Playlist object will be returned if success. None will be returned otherwise
    """
    try:
        # An error will be thrown if the input URL is invalid
        playlist = Playlist(url)

        # Use playlist.title to test if the playlist is viewable (publicly)
        ignored = playlist.title

        # All looks good and return the Playlist object
        return playlist
    except Exception as e:
        return None

def downloadLogging(stream, chunk, bytes_remaining):
    """
        Just a logging fucntion (callback function?) for downloading streams.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100

    s = f"Downloading ... {percentage:.1f}%"
    # print(colorizeString(s, CBP2077_PINK))
    print(s)

def getVideo(url) -> Union[YouTube, str]:
    """
        A YouTube() object will be returned if the video is downloadable
        Otherwise str()
    """
    streams = None

    try:
        v = YouTube(url, on_progress_callback=downloadLogging)
        
        # For testing if the video is downloadable
        title = v.title
        length = v.length
        streams = v.streams

    except RegexMatchError:
        return f"Invalid URL: {url}", streams
    
    except URLError:
        return "Please check your connection, or updating pytube via 'pip install -U pytube'", streams
    
    except VideoUnavailable:
        f"Unable to get info of video: {url}", streams
    
    except AttributeError:
        return "Unable to get streams. This might be issue of Pytube.", streams
    
    except AgeRestrictedError:
        # Might need to update this except block
        # Since there is a bypass_age_gate() method in YouTube()
        return f"Age restricted video: {url}", streams

    else:
        return v, streams
