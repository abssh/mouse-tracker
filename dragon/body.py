from calc.circle import draw_circle_with_center
from dragon import DragonStatics

from calc.geometric import Geometric
from pygame import Surface, Rect, draw


class DragonBody:
    def __init__(self, root: Surface, pos, lead):
        self.root = root
        self.pos = pos
        self.lead = lead
        self.core_size = DragonStatics.BodyCoreSize

    def update(self, dx, dy):
        g = Geometric(self.pos, self.lead.pos)

        if ((dx, dy) == (0, 0)) or abs(g.l - DragonStatics.SpineSpace) > 5:
            draw_circle_with_center(
            self.root,
            self.pos,
            self.core_size,
            DragonStatics.BodyCoreColor
        )
            return 0, 0

        gx, gy = g.align_vec(dx, dy)

        # TODO: make legs
        # f1, f2 = g.joints(10)

        cx, cy = self.pos
        nx, ny = cx + gx, cy + gy
        self.pos = (nx, ny)

        draw_circle_with_center(
            self.root,
            self.pos,
            self.core_size,
            DragonStatics.BodyCoreColor
        )

        return gx, gy

        