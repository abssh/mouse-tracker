from random import random

from pygame import Surface
from dragon import DragonStatics
from dragon.body import DragonBody
from dragon.head import DragonHead


class Dragon:

    def __init__(self, root: Surface, body_length=40):
        self.root = root
        pos = root.get_rect().center
        self.head = DragonHead(root, pos)

        self.body: list[DragonBody] = []
        x, y = pos

        lead = self.head
        for i in range(body_length):
            x += DragonStatics.SpineSpace

            if i % 3 == 0:
                part = DragonBody(root, (x,y), lead, True)
                self.body.append(part)
                lead = part
                continue

            part = DragonBody(root, (x, y), lead)
            self.body.append(part)

            lead = part

    def update(self, mx, my):
        dx, dy = self.head.update(mx, my)

        for p in self.body:
            dx, dy = p.update(dx, dy)
