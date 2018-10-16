from p5 import *
from math import pi
#朝顔　（固い絆）

class MorningGlory:
    def __init__(self):
        # Draw the outer circle
        fill(127)
        circle_center = (random_uniform(low = 300, high = 500), random_uniform(low = 300, high = 500))
        r1 = random_uniform(low=180, high=270)
        circle(circle_center, 2 * r1)
        # Draw the inner circle
        fill(220)
        r2 = (sin(0.94) - sqrt(2)*2/5) * r1
        circle(circle_center, 2 * r2)
        # Draw 5 circular sectors by using lines
        fill(0)
        for i in range(4):
            start = Vector((circle_center[0] +  r2 * cos(i * 0.4 * pi)), (circle_center[1] + r2 * sin(i * 0.4 * pi)))
            # start = ((circle_center[0] + r2 * cos(0.2 * pi)), (circle_center[1] + r2 * sin(0.2 * pi)))
            for angle in range(0, 150, 1):
                radian = radians(angle/2)
                end = Vector((circle_center[0] + r1 * cos(radian * i)), (circle_center[1] + r1 * sin(radian * i)))
                line(start, end)



def setup():
    size(800, 800)
    background(255)

# def draw():
    # if key == 'ENTER':
    #     # Draw the outer circle
    #     fill(127)
    #     r1 = random_uniform(low=200, high=600)
    #     circle((400, 400), r1)
    #     # Draw the inner circle
    #     fill(255)
    #     r2 = (sin(0.94) - sqrt(2)*2/5) * r1
    #     circle((400, 400), r2)
    #
    #     # Draw 5 circular sectors by using lines


def key_pressed():
    # for _ in range(0,4):
    #     MorningGlory()
    MorningGlory()

if __name__ == '__main__':
    run()
