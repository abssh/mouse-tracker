from calc.circle import draw_circle_with_center
from dragon import DragonStatics

from math import sqrt
from pygame import Rect, Surface, draw


class DragonHead:
    
    def __init__(self, root: Surface, pos):
        self.root = root
        self.pos = pos
        self.size = DragonStatics.HeadSize
    

    def update(self, mx, my) -> int:
        cx, cy = self.pos
        x, y = (mx - cx, my - cy)
        l = sqrt((x**2) + (y**2))/5
        dx, dy = (x/l), (y/l)
        
        if l < 0.9:
            dx, dy = 0, 0
        
        nx, ny = cx + dx, cy + dy

        draw_circle_with_center(
            self.root,
            (nx, ny),
            self.size,
            DragonStatics.HeadColor
            )

        
        self.pos = (nx, ny)

        return dx, dy