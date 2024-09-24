#!/usr/bin/env python

import os
import subprocess
import sys

import pytesseract

ACCEPTED_EXTENSIONS = ['jpg', 'jpeg', 'png']


def read_image(path: str, lang: str = 'por'):
    return pytesseract.image_to_string(path, lang)


def clear_path(path):
    for file in os.listdir(path):
        if len(file.split('.')) < 2:
            continue
        filename, ext = file.split('.')
        if 'converted' in filename or ext == 'txt':
            os.remove(os.path.join(path, file))


if __name__ == '__main__':

    args = sys.argv

    if len(args) == 1:
        print(
            'Arguments not passed!\n',
            '- Usage: scanner.py ./path/to/images [--clear]\n',
        )
        sys.exit(1)

    PATH = args[1]

    if '--clear' in args:
        print('cleaning...')
        clear_path(PATH)
        sys.exit()

    for file in sorted(os.listdir(PATH)):

        if len(file.split('.')) < 2:
            continue

        filename, ext = file.split('.')

        if ext.lower() not in ACCEPTED_EXTENSIONS:
            continue

        if (
            'converted' in filename
            or ext == 'txt'
            or os.path.exists(os.path.join(PATH, filename + '.txt'))
            or os.path.exists(
                os.path.join(PATH, filename + '_converted.' + ext)
            )
        ):
            continue

        print(file, 'processing...')

        subprocess.call(
            ' '.join(
                [
                    os.path.join(os.getcwd(), 'textcleaner'),
                    '-e normalize -f 15 -o 5 -S 200',
                    os.path.join(PATH, file),
                    os.path.join(PATH, filename + '_converted.' + ext),
                ]
            ),
            shell=True,
        )

        with open(os.path.join(PATH, filename + '.txt'), 'w') as out:
            out.write(
                read_image(os.path.join(PATH, filename + '_converted.' + ext))
            )
