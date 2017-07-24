import pygame
import math
class Julia(object):
    def __init__(self, width, height, colors, P, Q):
        self.size = self.width, self.height = width, height
        self.image = pygame.Surface(self.size)
        self.minX,self.maxX, self.minY, self.maxY = -1.5,1.5,-1.5,1.5
        self.deltaX = (self.maxX-self.minX)/width
        self.deltaY = (self.maxY-self.minY)/height
        self.max_iterations = 32
        self.radius = 2
        self.P = P
        self.Q = Q
        self.colors = colors
        self.color_density = 100
        self.rando=[]

    def calculate(self):
        color = self.colors[0]
        for col in range(int(-1*self.width/2), int(self.width/2)):
            for row in range(int(-1*self.height/2), int(self.height/2)):
                x = col * self.deltaX
                y = row * self.deltaY
                n = 0#[1,max_iterations]
                radius = x*x+y*y
                println = x==0.704 and y==0.904
                if println: self.rando.append((0,x,y))
                while n < self.max_iterations and radius <= self.radius:
                    n+=1
                    xn = x*x-y*y+self.P
                    yn = 2*x*y+self.Q
                    x=xn
                    y=yn
                    radius = x*x+y*y
                    if println:
                        self.rando.append((n,x,y))

                if radius < self.radius:
                    c_index = (int(radius *self.color_density))%(len(self.colors)-1)+1
                    color = self.colors[c_index]
                    #print('%f, radius: %f'%(c_index,radius))
                else:
                    color = self.colors[0]

                self.image.fill(color, rect=(col+self.width/2, row+self.height/2, 1, 1))
                #self.image.fill((55,255,155), rect=(0.704/self.deltaX+self.width/2, 0.904/self.deltaY+self.height/2, 5, 5))


    def printrando(self):
        for a in self.rando:
            print("%i : (x:%f+yi:%f)"%(a[0],a[1],a[2]))

    def update_constant(self, x, y):
        self.P=x
        self.Q=y
        self.calculate()
#     def window_resize(self, x,y,w,h):
#         self.minX,self.maxX, self.minY, self.maxY = x*self.deltaX,(x+w)*self.deltaX,y*self.deltaY,(y+h)*self.deltaY
#         self.deltaX = (self.maxX-self.minX)/self.width
#         self.deltaY = (self.maxY-self.minY)/self.height
