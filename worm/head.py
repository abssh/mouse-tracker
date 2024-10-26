from typing import Tuple, Any

from geometry.draw import draw_circle_with_center
from worm import WormStatics

from math import sqrt
from pygame import Surface


class WormHead:

    def __init__(self, root: Surface, pos):
        self.root = root
        self.pos = pos
        self.size = WormStatics.HeadSize

    def update(self, mx, my) -> tuple[int | float | Any, int | float | Any]:
        cx, cy = self.pos
        x, y = (mx - cx, my - cy)
        length = sqrt((x ** 2) + (y ** 2)) / 3
        dx, dy = (x / length), (y / length)

        if length < 0.9:
            dx, dy = 0, 0

        nx, ny = cx + dx, cy + dy

        draw_circle_with_center(
            self.root,
            (nx, ny),
            self.size,
            WormStatics.HeadColor
        )

        self.pos = (nx, ny)

        return dx, dy
