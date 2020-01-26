import os


def save_translate(filename, translate, directories=None):
    path = filename
    if directories:
        path = os.path.join(directories, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(translate)
