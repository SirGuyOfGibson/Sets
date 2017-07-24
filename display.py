import pygame

class Screen(object):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (247,247,48)

    SHOW_AXIS = False

    def __init__(self, screen_width, screen_height, bg_color=(64, 100, 191)):
        pygame.init()
        pygame.display.set_caption("Julia Sets")
        self.pygame = pygame
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(bg_color)
        self.screen.blit(self.background.convert(), (0,0))
        self.pygame.display.update()
        self.clock = self.pygame.time.Clock()
        self.duration = 1
        self.rendered = {'0background' : (self.background,0,0)}
        self.font = self.pygame.font.Font(None, 20)
        self.axis = self.pygame.Surface(self.screen.get_size())
        self.x_axis, self.y_axis = self.axis.get_width()/2, self.axis.get_height()/2
        self.pygame.mouse.set_visible(False)

    def run(self):
        self.running = True
    #Main Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #self.julia.window_resize(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 100, 100)
                    x,y=(pygame.mouse.get_pos()[0]-self.julia.width/2)*self.julia.deltaX, (pygame.mouse.get_pos()[1]-self.julia.height/2)*self.julia.deltaY
                    self.julia.update_constant(x,y)
                    self.blitscreen()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.__A_PRESS()
                    if event.key == pygame.K_q:
                        self.running = False

        #replace mouse with circle
            x,y = self.pygame.mouse.get_pos()
            circles = self.pygame.Surface((10,10))
            circles.fill(self.bg_color)
            circles.set_colorkey(self.bg_color)
            self.pygame.draw.ellipse(circles, self.BLUE, (0,0,10,10), 1)
            self.rendered['2circle'] = (circles, x-5,y-5)

        #display time
            time_ms = self.clock.tick(10)
            self.duration += time_ms/1000
            self.write('4text', "time  :  %.1f"%self.duration, 0, 0)
        #display complex constant x+yi
            self.write('5text', "constant: %0.4f + %0.4f i"%(self.julia.P,self.julia.Q), 0, 15)
        #display layers blitting
            layers = str(sorted(self.rendered))
            self.write('3text', "layers blitting:  %s"%layers, 0, self.y_axis*2-15)

            self.blitscreen()
        self.pygame.quit()

    def blitscreen(self):
        for surf in sorted(self.rendered):
            self.screen.blit(self.rendered[surf][0].convert(), (self.rendered[surf][1],self.rendered[surf][2]))
        self.pygame.display.flip()

    def show_layer(self, image):
        image.set_colorkey(self.bg_color)
        self.rendered['1image'] = (image,0,0)
        self.blitscreen()

    def draw_background(self, show_axis=SHOW_AXIS):
        area = pygame.Surface(self.screen.get_size())
        area.fill(self.bg_color)
        area.blit(self.background.convert(), (0,0))
        if show_axis:
            self.pygame.draw.line(area, self.WHITE, (self.x_axis,0),(self.x_axis, self.y_axis*2))
            self.pygame.draw.line(area, self.WHITE, (0,self.y_axis),(self.x_axis*2, self.y_axis))
        else:
            print('not showing axis')

        self.rendered['0background'] = (area,0,0)
        self.blitscreen()

    def write(self, textlayerkey, text, x, y):
        duration = self.font.render(text, False, self.BLACK)
        self.rendered[textlayerkey] = (duration, x, y)

    def save(self, name):
        self.pygame.image.save(self.screen,'Saved/'+name+'.bmp')


    def __A_PRESS(self):
        return None


































