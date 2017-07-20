import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Screen(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Julia Sets")
        self.pygame = pygame
        screen = pygame.display.set_mode((500, 300))
        background = pygame.Surface(screen.get_size())
        self.bg_color = self.R, self.G, self.B = 64, 100, 191
        background.fill((self.R, self.G, self.B))
        screen.blit(background.convert(), (0,0))
        pygame.display.update()
        self.screen = screen
        self.background = background
        self.clock = pygame.time.Clock()
        self.duration = 0
        self.rendered = {'0background' : (self.background,0,0)}
        self.font = pygame.font.Font(None, 20)
        self.axis = pygame.Surface(screen.get_size())
        self.x_axis, self.y_axis = self.axis.get_width()/2, self.axis.get_height()/2
        self.show_axis()
        pygame.mouse.set_visible(False)

    def run(self):
        self.running = True

    #Main Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #if event.type == pygame.MOUSEBUTTONDOWN:

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.__A_PRESS()
                    if event.key == pygame.K_q:
                        running = False

        #replace mouse with circle
            x,y = pygame.mouse.get_pos()
            circles = pygame.Surface((10,10))
            circles.fill(self.bg_color)
            circles.set_colorkey(self.bg_color)
            self.pygame.draw.ellipse(circles, BLUE, (0,0,10,10), 1)
            self.rendered['1circle'] = (circles, x-5,y-5)

        #display time
            time_ms = self.clock.tick(10)
            self.duration += time_ms/1000
            self.write('2text', "time  :  %.1f"%self.duration, 0, 0)
        #display layers blitting
            layers = str(sorted(self.rendered))
            self.write('3text', "layers blitting:  %s"%layers, 0, self.y_axis*2-15)

            self.blitscreen()

    def blitscreen(self):
        for surf in sorted(self.rendered):
            self.screen.blit(self.rendered[surf][0].convert(), (self.rendered[surf][1],self.rendered[surf][2]))
        self.pygame.display.flip()

    def show_axis(self, show=True):
        area = pygame.Surface(self.screen.get_size())
        area.blit(self.background.convert(), (0,0))
        if show:
            self.pygame.draw.line(area, WHITE, (self.x_axis,0),(self.x_axis, self.y_axis*2))
            self.pygame.draw.line(area, WHITE, (0,self.y_axis),(self.x_axis*2, self.y_axis))

        self.rendered['0background'] = (area,0,0)

    def write(self, textlayerkey, text, x, y):
        duration = self.font.render(text, False, BLACK)
        self.rendered[textlayerkey] = (duration, x, y)

    def save(self, name):
        pygame.image.save(self.background,name+'.bmp')


    def __A_PRESS(self):
        self.R, self.G, self.B = self.R+4, self.G+3, self.B-5




































