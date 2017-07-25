class Set(object):
    def __init__(self, size, rect, colors=None):#size(width,height), rect(xmin,ymind,xmax,ymax), colors(background, color1, color2,...)
        self.width,self.height = self.size = size
        self.xmin,self.ymin,self.xmax,self.ymax = rect
        self.xdim = (self.xmax-self.xmin)/self.width
        self.ydim = (self.ymax-self.ymin)/self.height
        self.max_iterations = 32
        self.colors = colors
        self.radius = 2 ##########!!!!!
        self.color_density = 100

    def resize_render(self, center, width, height):
        self.xmin,self.ymin = center[0]-(width/2), center[1]-(height/2)
        self.xmax,self.ymax = center[0]+(width/2), center[1]+(height/2)
        self.xdim = (self.xmax-self.xmin)/self.width
        self.ydim = (self.ymax-self.ymin)/self.height

    def render_onto_image(self, fill_func):
        for col in range(int(-1*self.width/2), int(self.width/2)):
            for row in range(int(-1*self.width/2), int(self.width/2)):
                fill_func(self.iterate_to_color(col, row), rect=(col+self.width/2, row+self.height/2, 1, 1))

    def iterate_to_color(self, x, y):
        return (0,0,0)