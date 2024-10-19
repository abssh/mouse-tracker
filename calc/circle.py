from pygame import Surface, Rect, draw


def draw_circle_with_center(root: Surface, center: tuple[int, int], size:int, color):
    rect = Rect(0, 0, size, size)
    rect.center = center
    draw.ellipse(
        root,
        color,
        rect
    )