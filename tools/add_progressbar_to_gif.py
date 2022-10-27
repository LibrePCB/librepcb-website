#!/usr/bin/env python

import sys
from PIL import Image, ImageDraw


BAR_HEIGHT = 2
BAR_COLOR = (255, 0, 0)
FADE_LENGTH = 0.05


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

    total_time = sum(durations)
    fade_length = FADE_LENGTH * im.size[0]

    out_frames = []
    for frame in frames:
        elapsed_time = sum(durations[:len(out_frames)])
        bar_length = int((elapsed_time * im.size[0]) / total_time)

        bar = Image.new('RGBA', frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(bar)
        for x in range(0, im.size[0]):
            fade_pos = (x - bar_length - (fade_length / 2)) / fade_length
            color = list(BAR_COLOR)
            color.append(max(0, min(255, int(255 * (1 - fade_pos)))))
            draw.line([(x, im.size[1] - BAR_HEIGHT), (x, im.size[1])],
                      tuple(color), 1, 'curve')

        frame.paste(bar, (0, 0), bar)
        out_frames.append(frame.convert('RGB'))

    out_frames[0].save(
        filename, save_all=True, loop=0, duration=durations,
        optimize=True, append_images=out_frames[1:],
    )
