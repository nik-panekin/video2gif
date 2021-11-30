import sys
import os

import ffmpeg

HELP = """Usage:
    video2gif.py <video filename> [fps]

Command-line parameters:
    <video filename> - input video file to be converted to gif;

    [fps] - frames per second for gif animation (optional).
"""

DEFAULT_FPS = 15

def check_params() -> bool:
    if len(sys.argv) < 2:
        print(HELP)
        return False

    if not os.path.exists(sys.argv[1]):
        print('Error: input file not found!')
        return False

    if len(sys.argv) > 2:
        if not sys.argv[2].isdigit():
            print('Error: FPS must be a number!')
            return False

        fps = int(sys.argv[2])
        if fps > 60 or fps < 1:
            print('Error: incorrect FPS value. FPS must be in range: [1...60]')
            return False

    return True

def main():
    if not check_params():
        return

    filename = sys.argv[1]
    fps = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_FPS

    stream = ffmpeg.input(filename)
    stream = ffmpeg.filter(stream, 'fps', fps)
    stream = ffmpeg.output(stream, os.path.splitext(filename)[0] + '.gif')
    ffmpeg.run(stream)

if __name__ == '__main__':
    main()
