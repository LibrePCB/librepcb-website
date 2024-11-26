#!/usr/bin/env python

import sys
from PIL import Image, ImageDraw, ImageEnhance


SIZE = 15
OFFSET = 3
COLOR = (0, 0, 0, 150)


if __name__ == '__main__':
    filename = sys.argv[1]
    im = Image.open(filename)
    frames = []
    durations = []
    for frame in range(0, im.n_frames):
        im.seek(frame)
        new_im = Image.new("RGBA", im.size)
        new_im.paste(im)
        frames.append(new_im)
        durations.append(im.info['duration'])

    durations[-1] = 1500
    total_time = sum(durations[:-1])
    overlay_scale = 50
    overlay_size = (SIZE * overlay_scale, SIZE * overlay_scale)
    overlay_rect = [(0, 0), overlay_size]
    overlay_position = (im.size[0] - OFFSET - SIZE, im.size[1] - OFFSET - SIZE)

    out_frames = []
    for frame in frames:
        elapsed_time = sum(durations[:len(out_frames)])
        angle = 360 * elapsed_time / total_time
        overlay = Image.new('RGBA', overlay_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        draw.ellipse(overlay_rect, None, COLOR, 1 * overlay_scale)
        draw.pieslice(overlay_rect, -90, angle - 90, COLOR)
        overlay = overlay.resize((SIZE, SIZE),
                                 resample=Image.Resampling.NEAREST)
        frame.paste(overlay, overlay_position, overlay)
        out_frames.append(frame.convert('RGB'))

    overlay = Image.open('tools/overlay.png')
    overlay_width = im.size[0] * 2 // 3
    overlay_height = (overlay.size[1] * overlay_width) // overlay.size[0]
    overlay_position = [
        (im.size[0] // 2) - (overlay_width // 2),
        (im.size[1] // 2) - (overlay_height // 2),
    ]
    overlay = overlay.resize((overlay_width, overlay_height),
                             resample=Image.Resampling.NEAREST)
    last_frame = Image.new('RGBA', im.size, (0, 0, 0, 0))
    last_frame.paste(out_frames[-1])
    brightness = ImageEnhance.Brightness(last_frame)
    last_frame = brightness.enhance(0.8)
    last_frame.paste(overlay, overlay_position, overlay)
    out_frames.append(last_frame.convert('RGB'))
    durations.append(1500)

    out_frames[0].save(
        filename, save_all=True, loop=0, duration=durations,
        optimize=True, append_images=out_frames[1:],
    )
