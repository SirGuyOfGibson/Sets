from set import Set

class Julia(Set):
    def __init__(self, size, rect, P, Q, colors=None):
        Set.__init__(self, size, rect, colors)
        self.P = P
        self.Q = Q

    def iterate_to_color(self, col, row):
        x = col * self.xdim
        y = row * self.ydim
        n = 0#[1,max_iterations]
        radius = x*x+y*y
        while n < self.max_iterations and radius <= self.radius:
            n+=1
            xn = x*x-y*y+self.P
            yn = 2*x*y+self.Q
            x=xn
            y=yn
            radius = x*x+y*y

        color = self.colors[0]

        if radius < self.radius:
             c_index = (int(radius *self.color_density))%(len(self.colors)-1)+1
             color = self.colors[c_index]

        return color

    def update_constant(self, x, y):
        self.P=x
        self.Q=y

#     def window_resize(self, x,y,w,h):
#         self.minX,self.maxX, self.minY, self.maxY = x*self.deltaX,(x+w)*self.deltaX,y*self.deltaY,(y+h)*self.deltaY
#         self.deltaX = (self.maxX-self.minX)/self.width
#         self.deltaY = (self.maxY-self.minY)/self.height
