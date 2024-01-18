import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the size of the rain
RAINSIZE = 10000

# Define the structure for a raindrop

class Raindrop:
    def __init__(self):
        self.x = random.uniform(-100, 100)
        self.y = random.uniform(-100, 100)
        self.z = random.uniform(-100, 100)
        self.speed = random.uniform(0.05, 0.1)

    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glPointSize(5.0)  # Set this to the desired size
        glBegin(GL_POINTS)
        glVertex3f(self.x, self.y, self.z)
        glEnd()
        self.update()

    def update(self):
        self.y -= self.speed
        if self.y < -1:
            self.y = 100


# Create a list of raindrops
raindrops = [Raindrop() for _ in range(RAINSIZE)]

def generate_rain():
    # Generate the rain
    for drop in raindrops:
        drop.draw()
