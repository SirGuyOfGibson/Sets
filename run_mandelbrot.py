import pygame
from mandelbrot import Mandelbrot
from display import Screen
from threading import Thread

if __name__ == '__main__':

    size = (screen_width, screen_height) = (500, 500)
    rect = (-2,-2,2,2)
    colors = [Screen.BLACK,Screen.RED,Screen.GREEN,Screen.BLUE,Screen.YELLOW,Screen.WHITE]
    screen_running = True
    show_axis=True

    display = Screen(screen_width,screen_height)
    display.running = screen_running
    mandel = Mandelbrot(size, rect, colors)

    MAIN_THREAD = Thread(target=display.run)
    MAIN_THREAD.setDaemon(True)
    MAIN_THREAD.start()

    display.draw_background(show_axis)
    mandel.render_image()
    display.show_layer(mandel.image)