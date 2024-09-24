import os
import subprocess
import sys

import pytesseract


def read_image(path: str, lang: str = 'por'):
    return pytesseract.image_to_string(path, lang)


def clear_path(path):
    for file in os.listdir(path):
        ext = file.split('.')[1]
        if ext in ['txt', 'converted']:
            os.remove(os.path.join(path, file))


if __name__ == '__main__':

    args = sys.argv

    PATH = args[1]

    if '--clear' in args:
        print('cleaning...')
        clear_path(PATH)
        sys.exit()

    for file in sorted(os.listdir(PATH)):

        if len(file.split('.')) == 3:
            continue

        filename, ext = file.split('.')

        if (
            ext in ['txt', 'converted']
            or os.path.exists(os.path.join(PATH, filename + '.txt'))
            or os.path.exists(
                os.path.join(PATH, filename + '.converted.' + ext)
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
                    os.path.join(PATH, filename + '.converted.' + ext),
                ]
            ),
            shell=True,
        )

        with open(os.path.join(PATH, filename + '.txt'), 'w') as out:
            out.write(
                read_image(os.path.join(PATH, filename + '.converted.' + ext))
            )
