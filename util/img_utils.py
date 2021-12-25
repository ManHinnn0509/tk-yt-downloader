import io
import base64
import requests as req

from typing import Union
from PIL import Image, ImageTk

# Use Image.NEAREST (0), Image.LANCZOS (1), Image.BILINEAR (2), Image.BICUBIC (3), Image.BOX (4) or Image.HAMMING (5)
RESAMPLING_FILTER_DOWNSCALING = Image.LANCZOS

def imgFromBase64(b64Str: str, resizeToPixel_x=None, resizeToPixel_y=None):
    try:
        b = base64.b64decode(b64Str)
        return __processImage(b, resizeToPixel_x, resizeToPixel_y)
    except:
        return None
    
def getImgFromURL(url: str, resizeToPixel_x=None, resizeToPixel_y=None):
    try:
        r = req.get(url)
        b = r.content

        return __processImage(b, resizeToPixel_x, resizeToPixel_y)
    except Exception as e:
        # print(e)
        return None

def readImgFromPath(p: str, resizeToPixel_x=None, resizeToPixel_y=None):
    try:
        b = None
        with open(p, 'rb') as f:
            b = f.read()
        
        return __processImage(b, resizeToPixel_x, resizeToPixel_y)
    except Exception as e:
        # print(e)
        return None

def __processImage(b: bytes, resizeToPixel_x=None, resizeToPixel_y=None):
    try:
        im = Image.open(io.BytesIO(b))
        if (resizeToPixel_x != None and resizeToPixel_y != None):
            temp = im.resize((resizeToPixel_x, resizeToPixel_y), resample=RESAMPLING_FILTER_DOWNSCALING)
            im = temp
                
        img = ImageTk.PhotoImage(im)
        return img
    except:
        return None