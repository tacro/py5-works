from p5 import *

"""
"she's never gonna be mine."

a lot of particles moving vertically-spiral.
they go far when user apoproaches them (presses key).
"""

class RotatingParticles:
    def __init__(self, windowSize, color):
        width = windowSize.x
        height = windowSize.y
        fill(color)
        for y in range(0, height, 10):
            numOfParticles = int(random_uniform(low = 10, high = 200))
            for x in range(numOfParticles):
                
                radius = noise(random_uniform(low = 1, high = x/3))
