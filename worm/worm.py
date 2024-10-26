from random import random

from pygame import Surface
from worm import WormStatics
from worm.body import WormBody
from worm.head import WormHead


class Worm:

    def __init__(self, root: Surface, body_length=40):
        self.root = root
        pos = root.get_rect().center
        self.head = WormHead(root, pos)

        self.body: list[WormBody] = []
        x, y = pos

        lead = self.head
        for i in range(body_length):
            x += WormStatics.SpineSpace

            if i % 3 == 0:
                part = WormBody(root, (x, y), lead, True)
                self.body.append(part)
                lead = part
                continue

            part = WormBody(root, (x, y), lead)
            self.body.append(part)

            lead = part

    def update(self, mx, my):
        dx, dy = self.head.update(mx, my)

        for p in self.body:
            dx, dy = p.update(dx, dy)
