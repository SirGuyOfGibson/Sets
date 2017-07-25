import math
from set import Set

class Mandelbrot(Set):
    def __init__(self, size, rect, colors=None):
        Set.__init__(self, size, rect, colors)

    def iterate_to_color(self, col, row):
        a = col * self.xdim
        b = row * self.ydim
        x = 0
        y = 0
        n = 0
        radius = x*x+y*y
        color = self.colors[0]
        while n < self.max_iterations and radius <= self.radius:
            n += 1
            xn = x*x-y*y+a
            yn = 2*x*y+b
            x=xn
            y=yn
            radius=xn*xn+yn*yn

        if radius > self.radius:
            c_index = (int(radius *(len(self.colors)-1)))%(len(self.colors)-1)+1
            color = self.colors[c_index]

        return color
