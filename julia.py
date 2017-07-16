import pygame
import math
class Julia(object):
    def __init__(self, width, height, colors, P, Q):
        self.size = self.width, self.height = width, height
        self.image = pygame.Surface(self.size)
        self.minX,self.maxX, self.minY, self.maxY = -1.8, 1.8, -1.2, 1.2
        self.deltaX = (self.maxX-self.minX)/width
        self.deltaY = (self.maxY-self.minY)/height
        self.max_iterations = 64
        self.maxSize = 4
        self.P = P
        self.Q = Q
        self.colors = colors
        self.cs = 1000

    def calculate(self):
        color = self.colors[0]
        for col in range(int(-1*self.width/2), int(self.width/2)):
            for row in range(int(-1*self.height/2), int(self.height/2)):
                x = col * self.deltaX
                y = row * self.deltaY
                iters = 0
                while iters < self.max_iterations and x*x+y*y < self.maxSize:
                    iters+=1
                    x = x*x - y*y + self.P
                    y = 2*x*y + self.Q
                if iters == self.max_iterations:
                    color = self.colors[int(math.sqrt(x*x+y*y*self.cs))%(len(self.colors)-1)+1]
                else:
                    color = self.colors[0]
                self.image.fill(color, rect=(col+self.width/2, row+self.height/2, 1, 1))
