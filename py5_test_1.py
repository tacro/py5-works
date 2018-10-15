from p5 import *

def setup():
    size(640, 640)
    no_stroke()
    background(255)

def draw():
    if mouse_is_pressed:
        fill(255, 207, 53, 127)
        circle_size = random_uniform(low=5, high=15)
        circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(0)

run()
