from p5 import *

"""
"she's never gonna be mine."

a lot of particles moving vertically-spiral.
they go far when user apoproaches them (presses key).
"""

class RotatingParticles:
    def __init__(self, w, h, color):
        width = w
        height = h
        fill(color)
        for y in range(0, height, 5):
            numOfParticles = int(random_uniform(low = 5, high = 8))
            for x in range(numOfParticles):
                r = random_uniform(low = 0, high = width/3)
                pos_x = random_uniform(low = width/2 - r, high = width/2 + r)
                center = Vector(pos_x , y * random_uniform(low = 0.9, high = 1.1))
                circle(center, 3)



window_w = 800
window_h = 800

def setup():
    size(window_w, window_h)
    background(0)

def draw():
    no_stroke()
    background(0)
    RotatingParticles(window_w, window_h, 255)

if __name__ == '__main__':
    run()
