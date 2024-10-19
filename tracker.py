from math import sqrt
import pygame
from pygame import Surface, Rect, draw


class Tracker():
    def __init__(self, root: Surface):
        self.root = root
        self.x, self. y = root.get_rect().center

    
    def update(self, mx, my):
        cx, cy = self.x, self.y
        x, y = (mx - cx, my - cy)
        l = sqrt((x**2) + (y**2))/5
        dx, dy = (x/l), (y/l)
        
        if l < 0.9:
            dx, dy = 0, 0
        
        nx, ny = cx + dx, cy + dy
        
        _rect = Rect(nx - 10, ny -10, 20, 20)
        draw.ellipse(
            self.root,
            (0, 75, 200),
            _rect
            )
        
        self.x , self.y = nx, ny

        

    