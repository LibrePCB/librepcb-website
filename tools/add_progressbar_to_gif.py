#!/usr/bin/env python

import sys
from PIL import Image


BAR_HEIGHT = 2
BAR_COLOR = (100, 100, 100, 200)

if __name__ == '__main__':
    filename = sys.argv[1]
    im = Image.open(filename)
    frames = []
    durations = []
    for frame in range(0, im.n_frames):
        im.seek(frame)
        durations.append(im.info['duration'])
        new_im = Image.new("RGBA", im.size)
        new_im.paste(im)
        frames.append(new_im)

    out_frames = []
    for frame in frames:
        elapsed_time = sum(durations[:len(out_frames)])
        total_time = sum(durations)
        bar_length = int((elapsed_time * im.size[0]) / total_time)
        bar = Image.new('RGBA', (bar_length, BAR_HEIGHT), BAR_COLOR)
        frame.paste(bar, (0, im.size[1] - BAR_HEIGHT), bar)
        out_frames.append(frame)

    out_frames[0].save(
        filename, save_all=True, loop=0, duration=durations,
        append_images=out_frames[1:],
    )
