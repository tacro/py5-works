from p5 import *

x = 100
y = 100

xspeed = random_uniform(low=1, high=5)
yspeed = random_uniform(low=7, high=15)

def setup():
    size(800, 800)
    background(0)

def draw():
    global x
    global y
    global xspeed
    global yspeed

    no_stroke()
    fill(255, 10)
    rect((0, 0), width, height)

    # add the current speed to the location
    x = x + xspeed
    y = y + yspeed

    if x > width or x < 0:
        xspeed = -xspeed

    if y > height or y < 0:
        yspeed = -yspeed

    stroke(255)
    fill(255, 207, 53)
    circle_size = 15
    circle((x, y), circle_size)

if __name__ == '__main__':
    run()
