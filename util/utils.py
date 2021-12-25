def genLabelText(l: list, pad=''):
    """
        Generates multiline label for Frames
    """
    pad = str(pad)
    temp = [pad + str(i) for i in l]
    return '\n'.join(temp)