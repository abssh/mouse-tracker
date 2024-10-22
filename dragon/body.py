from math import pi, sqrt

from geometry.draw import draw_circle_with_center, draw_line
from dragon import DragonStatics

from geometry.geometric import Geometric
from pygame import Surface


class DragonBody:
    def __init__(self, root: Surface, pos, lead, has_leg: bool = False):
        self.root = root
        self.pos = pos
        self.lead = lead
        self.core_size = DragonStatics.BodyCoreSize
        self.has_leg = has_leg

        self.leg_status = 0
        self.leg_target_l = (0, 0)
        self.leg_target_r = (0, 0)
        self.leg_pos_l = (0, 0)
        self.leg_pos_r = (0, 0)

    def update(self, dx, dy):
        g = Geometric(self.pos, self.lead.pos)

        if ((dx, dy) == (0, 0)) or abs(g.lv - DragonStatics.SpineSpace) > 5:
            draw_circle_with_center(
                self.root,
                self.pos,
                self.core_size,
                DragonStatics.BodyCoreColor
            )
            self.draw_skeleton(g)
            if self.has_leg:
                self.create_legs(g)
            return 0, 0

        gx, gy = g.align_vec(dx, dy)

        cx, cy = self.pos
        nx, ny = cx + gx, cy + gy
        self.pos = (nx, ny)

        draw_circle_with_center(
            self.root,
            self.pos,
            self.core_size,
            DragonStatics.BodyCoreColor
        )
        self.draw_skeleton(g)
        if self.has_leg:
            self.create_legs(g)

        return gx, gy

    def create_legs(self, g: Geometric):
        f1, f2 = g.joints(self.core_size / 2)
        draw_circle_with_center(
            self.root,
            f1,
            DragonStatics.CoreJointSize,
            DragonStatics.CoreJointColor
        )

        draw_circle_with_center(
            self.root,
            f2,
            DragonStatics.CoreJointSize,
            DragonStatics.CoreJointColor
        )
        knee_pos_l = (0, 0)
        knee_pos_r = (0, 0)

        if self.leg_status == 0:
            self.leg_pos_l = g.line_vector_ratio((0, -2), DragonStatics.LegLength * sqrt(2))
            self.leg_pos_r = g.line_vector_ratio((0, 2), DragonStatics.LegLength * sqrt(2))
            self.leg_status = 1

        if self.leg_status == 1:
            try:
                knee_pos_l = g.knee_point(self.leg_pos_l, DragonStatics.LegLength)
                knee_pos_r = g.knee_point(self.leg_pos_r, DragonStatics.LegLength)
            except ValueError:
                self.leg_status = 2

        if self.leg_status == 2:
            self.leg_target_l =g.line_vector_ratio((0, 2), DragonStatics.LegLength * sqrt(2))
            self.leg_target_r = g.line_vector_ratio((0, -2), DragonStatics.LegLength * sqrt(2))

            self.leg_pos_l, ok1 = g.move_to(self.leg_target_l, self.leg_pos_l)
            self.leg_pos_r, ok2 = g.move_to(self.leg_target_r, self.leg_pos_r)

            knee_pos_l = g.knee_point(self.leg_pos_l, DragonStatics.LegLength)
            knee_pos_r = g.knee_point(self.leg_pos_r, DragonStatics.LegLength)

            if ok2 or ok1:
                self.leg_status = 0


        draw_line(
            self.root,
            knee_pos_l,
            self.leg_pos_l,
            DragonStatics.LegColor,
            4
        )

        draw_line(
            self.root,
            knee_pos_r,
            self.leg_pos_r,
            DragonStatics.LegColor,
            4
        )

        draw_line(
            self.root,
            f1,
            knee_pos_r,
            DragonStatics.LegColor,
            4
        )
        draw_line(
            self.root,
            f2,
            knee_pos_l,
            DragonStatics.LegColor,
            4
        )

    def draw_skeleton(self, g: Geometric):
        p1 = g.line_vector_ratio(DragonStatics.SkeletonVectorRatioU, DragonStatics.SkeletonHeight)
        p2 = g.line_vector_ratio(DragonStatics.SkeletonVectorRatioD, DragonStatics.SkeletonHeight)
        draw_line(self.root, self.pos, p1, DragonStatics.SkeletonColor, DragonStatics.SkeletonWidth)
        draw_line(self.root, self.pos, p2, DragonStatics.SkeletonColor, DragonStatics.SkeletonWidth)
