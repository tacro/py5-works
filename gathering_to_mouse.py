from p5 import *

num_movers =600
movers = []

class Mover:
    def __init__(self):
        self.location = Vector(random_uniform(width),
                               random_uniform(height))

        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.top_speed = 40

    def update(self):
        # our algorithm for calculating acceleration
        mouse = Vector(mouse_x, mouse_y)

        # find vector pointing towards the mouse
        direction = mouse - self.location

        # normalize
        direction.normalize()

        # scale
        direction = direction * 0.5

        # set acceleration
        self.acceleration = direction;

        self.velocity = self.velocity + self.acceleration
        self.velocity.limit(self.top_speed)
        self.location = self.location + self.velocity

    def display(self):
        stroke(0)
        fill(20, random_uniform(low = 160, high = 200), random_uniform(low = 200, high = 250))
        circle(self.location, 5)

    def check_edges(self):
        if self.location.x > width:
            self.location.x = 0

        if self.location.x < 0:
            self.location.x = width

        if self.location.y > height:
            self.location.y = 0

        if self.location.y < 0:
            self.location.y = height

def setup():
    size(800, 800)
    background(0)

    # creating many mover objects
    for _ in range(num_movers):
        movers.append(Mover())

def draw():
    no_stroke()
    fill(0)
    rect((0, 0), width, height)

    # call functions on all objects in the array
    for mover in movers:
        mover.update()
        mover.check_edges()
        mover.display()

if __name__ == '__main__':
    run()
