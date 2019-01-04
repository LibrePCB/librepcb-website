#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import imageio
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Screencast:
    def __init__(self):
        self._screenshots = list()
        self._durations = list()
        self._current_screenshot = None
        self._cursor_x = 0
        self._cursor_y = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def add_screenshot(self, screenshot, duration, cursor=False):
        self.set_screenshot(screenshot)
        if cursor:
            screenshot.add_cursor(self._cursor_x, self._cursor_y)
        self._screenshots.append(screenshot)
        self._durations.append(duration)

    def set_screenshot(self, screenshot):
        self._current_screenshot = screenshot.copy()

    def add_delay(self, duration):
        self._durations[-1] += duration

    def set_cursor_pos(self, x, y):
        self._cursor_x = x
        self._cursor_y = y

    def move_cursor(self, x, y):
        PIXELS_PER_SECOND = 350
        FRAMES_PER_SECOND = 25
        dx = x - self._cursor_x
        dy = y - self._cursor_y
        distance = math.sqrt((dx**2) + (dy**2))
        duration = distance / PIXELS_PER_SECOND
        count = int(duration * FRAMES_PER_SECOND)
        for i in range(count + 1):
            px = int(self._cursor_x + (dx * i / count))
            py = int(self._cursor_y + (dy * i / count))
            screenshot = self._current_screenshot.copy()
            screenshot.add_cursor(px, py)
            self._screenshots.append(screenshot)
            self._durations.append(duration / count)
        self.set_cursor_pos(x, y)

    def cursor_click(self):
        screenshot = self._current_screenshot.copy()
        screenshot.add_cursor(self._cursor_x, self._cursor_y)
        self._screenshots.append(screenshot)
        self._durations.append(0.3)
        screenshot = self._current_screenshot.copy()
        screenshot.add_circle(self._cursor_x, self._cursor_y, 20,
                              fill=(255, 255, 0, 170))
        screenshot.add_cursor(self._cursor_x, self._cursor_y)
        self._screenshots.append(screenshot)
        self._durations.append(0.3)
        screenshot = self._current_screenshot.copy()
        screenshot.add_cursor(self._cursor_x, self._cursor_y)
        self._screenshots.append(screenshot)
        self._durations.append(0.3)

    def save(self, output, scale=1.0):
        abspath = os.path.join(ROOT_DIR, 'output', output)
        os.makedirs(os.path.dirname(abspath), exist_ok=True)
        imageio.mimsave(abspath, self._get_images(scale=scale),
                        duration=self._durations, palettesize=256,
                        subrectangles=True)

    def _get_images(self, scale=1.0):
        return [imageio.imread(screenshot.to_png(scale=scale), format='png')
                for screenshot in self._screenshots]
