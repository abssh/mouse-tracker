from math import sqrt


class Geometric:

    def __init__(self, p1, p2: tuple[float, float]):
        

        x1, y1 = p1
        x2, y2 = p2

        self.p1 = p1
        self.p2 = p2
        
        self.b = round(y2 - y1, 5)
        self.a = round(x2 - x1, 5)
        self.l = sqrt((self.b**2) + (self.a**2))

        self.c = self.a * y1 - self.b * x1
    

    
    def joints(self, r):
        a, b = self.a, self.b
        bx, by = self.p1

        if b == 0:
            return (bx, by -r), (bx, by +r)
        
        c2 = b*by + a*bx
        c3 = c2/b -(by)

        d1 =  1 + (a*a)/(b*b)
        d2 = -(2*bx) - (2*c3*a/(b))
        d3 = (bx*bx) + (c3*c3) - (r*r)
        
        if d2*d2 - (4*d1*d3) < 0:
            print("delta is negative, a, b, c2, c3:", a, b, c2, c3)
        delta = sqrt(d2*d2 - (4*d1*d3)) / (2*d1)

        const = (-d2) / (2*d1)


        x1, x2 =  const + delta, const - delta

        y1 = self.yn(x1)
        y2 = self.yn(x2)

        return (x1, y1), (x2, y2)

        

    def yn(self, xn):
        a, b = self.a, self.b
        bx, by = self.p1

        c2 = (b*by + a*bx)

        return ((-a*xn) + c2) / b
    

    def align_vec(self, dx, dy):
        lv = sqrt((dx**2) + (dy**2))

        dot = (dx*self.a) + (dy * self.b)
        
        lm = dot/ (self.l**2)

        return self.a * lm, self.b * lm

