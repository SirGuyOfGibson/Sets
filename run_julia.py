import pygame
from julia import Julia
from display import Screen
from threading import Thread

screen_width = 1000
screen_height = 1000
screen_running = True
show_axis=True

p_i, q_i = -0.904,0.224

display = Screen(screen_width, screen_height)
julia = Julia(screen_width, screen_height, [display.bg_color,display.RED,display.WHITE,display.YELLOW,display.GREEN,display.BLUE],p_i,q_i)
display.julia = julia
display.running = screen_running
MAIN_THREAD = Thread(target=display.run)
MAIN_THREAD.setDaemon(True)
MAIN_THREAD.start()

def update():
    display.draw_background(show_axis)
    julia.calculate()
    display.show_layer(julia.image)

def p(p):
    julia.P=p
def q(q):
    julia.Q=q

