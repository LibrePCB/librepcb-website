#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from mss import mss, tools
from PIL import Image, ImageDraw
from config import config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CURSOR_FILE = os.path.join(ROOT_DIR, 'cursor.png')


class Screenshot:
    def __init__(self, image, offset_top=0):
        self.image = image
        self.offset_top = offset_top

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def copy(self):
        return Screenshot(self.image.copy(), self.offset_top)

    def add_cursor(self, x, y):
        pos = (x, y + self.offset_top)
        cursor = Image.open(CURSOR_FILE)
        self.image.paste(cursor, box=pos, mask=cursor)

    def add_circle(self, x, y, radius, width=0, outline=None, fill=None):
        tmp = Image.new('RGBA', self.image.size, (0,0,0,0))
        p1 = (x - radius, y + self.offset_top - radius)
        p2 = (x + radius, y + self.offset_top + radius)
        draw = ImageDraw.Draw(tmp)
        draw.ellipse((p1, p2), width=width, outline=outline, fill=fill)
        self.image = Image.alpha_composite(self.image, tmp)

    def to_png(self, scale=1.0):
        image = self.image
        if scale != 1.0:
            size = (int(image.size[0] * scale), int(image.size[1] * scale))
            image = image.resize(size, resample=Image.LANCZOS)
        buffer = io.BytesIO()
        image.quantize(colors=256).save(buffer, format='png')
        return buffer.getvalue()

    def save(self, output, scale=1.0):
        abspath = os.path.join(ROOT_DIR, 'output', output)
        os.makedirs(os.path.dirname(abspath), exist_ok=True)
        with open(abspath, mode='wb') as f:
            f.write(self.to_png(scale=scale))

    @staticmethod
    def region(x, y, w, h, offset_top=0):
        with mss() as sct:
            sct_img = sct.grab({'left': x, 'top': y, 'width': w, 'height': h})
            img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            return Screenshot(img.convert(mode='RGBA'), offset_top)

    @staticmethod
    def window(funq_widget):
        properties = funq_widget.properties()
        return Screenshot.region(
            properties['x'],
            properties['y'],
            properties['width'],
            properties['height'] + config['TITLE_BAR_HEIGHT'],
            offset_top=config['TITLE_BAR_HEIGHT']
        )
