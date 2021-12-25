import time

def genLabelText(l: list, pad=''):
    """
        Generates multiline label for Frames
    """
    pad = str(pad)
    temp = [pad + str(i) for i in l]
    return '\n'.join(temp)


def formatTime(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))