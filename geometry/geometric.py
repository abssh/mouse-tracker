from math import sqrt, atan2, tan, cos, sin, asin, atan2, pi, atan2, radians
from time import sleep


class Geometric:

    def __init__(self, p1, p2: tuple[float, float]):
        x1, y1 = p1
        x2, y2 = p2

        self.p1 = p1
        self.p2 = p2

        self.b = y2 - y1
        self.a = x2 - x1
        self.lv = self.length(self.a, self.b)

        self.c = self.a * y1 - self.b * x1

    def joints(self, r):
        a, b = round(self.a, 3), round(self.b, 3)
        bx, by = self.p1

        if b == 0:
            return (bx, by - r), (bx, by + r)

        c2 = b * by + a * bx
        c3 = c2 / b - by

        d1 = 1 + (a * a) / (b * b)
        d2 = -(2 * bx) - (2 * c3 * a / b)
        d3 = (bx * bx) + (c3 * c3) - (r * r)

        # if d2 * d2 - (4 * d1 * d3) < 0:
        #     print("delta is negative, a, b, c2, c3:", a, b, c2, c3)
        delta = sqrt(d2 * d2 - (4 * d1 * d3)) / (2 * d1)

        const = (-d2) / (2 * d1)

        x1, x2 = const + delta, const - delta

        y1 = self.yn(x1)
        y2 = self.yn(x2)

        return (x1, y1), (x2, y2)

    def yn(self, xn):
        a, b = self.a, self.b
        bx, by = self.p1

        c2 = (b * by + a * bx)

        return ((-a * xn) + c2) / b

    def align_vec(self, dx, dy):
        dot = (dx * self.a) + (dy * self.b)
        lm = dot / (self.lv ** 2)

        return self.a * lm, self.b * lm

    def line_vector_ratio(self, ratio: tuple[int, int], length):
        r1, r2 = ratio
        a, b, l = self.a, self.b, self.lv
        x1, y1 = self.p1

        v1 = (a, b)
        v2 = (-b, a)

        vsx, vsy = ((v1[0] * r1) + (v2[0] * r2), (v1[1] * r1) + (v2[1] * r2))

        lvs = sqrt(vsx ** 2 + vsy ** 2)
        dx = vsx * length / lvs
        dy = vsy * length / lvs
        return x1 + dx, y1 + dy

    def knee_point(self, feet: tuple, length: int):
        a, b = self.a, self.b
        x1, y1 = self.p1

        fx, fy = feet

        v2 = ((x1 - fx), (y1 - fy))
        lv2 = self.length(*v2)

        d = sqrt((length ** 2) - ((lv2 / 2) ** 2))
        dv = (a * d/self.lv, b * d/self.lv)

        midd = x1 - v2[0] / 2, y1 - v2[1] / 2
        return midd[0] + dv[0], midd[1] + dv[1]

    def move_to(self, tpos, cpos):
        mx, my = tpos
        cx, cy = cpos
        x, y = (mx - cx, my - cy)
        step = self.length(x, y) / 4
        dx, dy = (x / step), (y / step)
        if step < 0.9:
            return (cx, cy), False

        nx, ny = cx + dx, cy + dy
        return (nx, ny), True

    @staticmethod
    def length(x, y):
        return sqrt(x ** 2 + y ** 2)
