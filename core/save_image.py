from uuid import uuid4
import os


def save_image(folder_name, filename):
    filename = filename.split('.')
    if len(filename) > 1:
        ext = filename[-1]
    else:
        ext = 'png'
    return os.path.join(folder_name, uuid4().hex + '.' + ext)