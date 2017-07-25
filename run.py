#!/bin/sh
#
#python3 -iBc 'from run_julia import julia, display, p, q, update
#update()'

from mandelbrot import Mandelbrot
from julia import Julia
from display import Screen
from threading import Thread
import pygame

if __name__ == '__main__':

    screen_size = (screen_width, screen_height) = (1000, 500)
    fractal_size = (-2,-2,2,2)
    color_scheme = [Screen.BLACK,Screen.RED,Screen.GREEN,Screen.BLUE,Screen.YELLOW,Screen.WHITE]
    screen_running = True

    display = Screen(screen_width,screen_height)
    display.running = screen_running
    mandel = Mandelbrot((screen_width/2,screen_height), fractal_size, color_scheme)
    julia = Julia((screen_width/2,screen_height), fractal_size, 0,0, color_scheme)
    display.sets.append(mandel)
    display.sets.append(julia)

    MAIN_THREAD = Thread(target=display.run)
    MAIN_THREAD.setDaemon(True)
    MAIN_THREAD.start()

    display.draw_set(mandel,0,0)
    display.draw_set(julia,screen_width/2,0)

    print('click anywhere on mandelbrot set near perimeter')
