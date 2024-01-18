import random
import math
import numpy as np
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from textures import *

# Define the size of the rain
RAINSIZE = 10000

shapes = []

def draw_scene():
    for shape in shapes:
        shape.draw()

class Object:
    def __init__(self, vertices, faces, textures=None):
        self.vertices = vertices
        self.faces = faces
        self.textures = textures

    def draw(self):
        for i, face in enumerate(self.faces):
            if self.textures is not None and len(self.textures) == len(self.faces):
                use_texture(self.textures[i])
            elif self.textures is not None and len(self.textures) == 1 : 
                use_texture(self.textures[0])
            glBegin(GL_POLYGON)
            tex_coords = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]
            for j, vertex in enumerate(face):
                glTexCoord2fv(tex_coords[j % 4])
                glVertex3fv(self.vertices[vertex])
            glEnd()
    
    def __eq__(self, other):
        if isinstance(other, Object):
            return self.vertices == other.vertices and self.faces == other.faces and self.textures == other.textures
        return False


class Cylinder(Object):
    def __init__(self, x, y, z, radius=1, height=1, num_segments=20, textures=None):
        self.vertices = []
        self.faces = []
        self.textures = textures

        for i in range(num_segments):
            theta = (math.pi * 2) * i / num_segments
            dx = radius * math.cos(theta)
            dz = radius * math.sin(theta)

            self.vertices.append([x + dx, y, z + dz])
            self.vertices.append([x + dx, y + height, z + dz])

        for i in range(0, num_segments * 2, 2):
            self.faces.append((i, (i + 2) % (num_segments * 2),
                              (i + 3) % (num_segments * 2), i + 1))
            self.faces.append((i, i + 1, (i + 3) %
                              (num_segments * 2), (i + 2) % (num_segments * 2)))


class Cube(Object):
    def __init__(self, x, y, z, width=1, height=1, depth=1, textures=None):
        self.vertices = [
            [x, y, z], [x, y + height, z], [x + width,
                                            y + height, z], [x + width, y, z],
            [x, y, z + depth], [x, y + height, z + depth], [x + width,
                                                            y + height, z + depth], [x + width, y, z + depth]
        ]
        self.faces = [
            (0, 1, 3, 2), (3, 2, 6, 7), (7, 6, 5,
                                         4), (4, 5, 1, 0), (1, 5, 6, 2), (4, 0, 3, 7)
        ]
        self.textures = textures


class HouseRoof(Object):
    def __init__(self, x, y, z, width=1, height=1, depth=1, textures=None):
        self.vertices = [
            [x, y, z], [x + width, y, z], [x, y + height, z+depth/2],
            [x + width, y + height, z+depth/2], [x, y,
                                                 z + depth], [x + width, y, z + depth]
        ]
        self.faces = [
            (0, 1, 3, 2), (0, 1, 5, 4), (4, 5, 3, 2), (0, 2, 4), (1, 3, 5)
        ]
        self.textures = textures


class Wave(Object):
    def __init__(self, x, y, z, width=10, depth=10, amplitude=1, frequency=1, textures=None):
        self.textures = textures
        self.amplitude = amplitude
        self.frequency = frequency
        self.width = width
        self.depth = depth
        self.x = x
        self.y = y
        self.z = z
        self.update()

    def update(self):
        self.vertices = []
        self.faces = []

        t = time.time()
        for i in range(self.width):
            for j in range(self.depth):
                wave_height = self.amplitude * \
                    np.sin(2 * np.pi * self.frequency * np.sqrt(i**2 + j**2) + t)
                self.vertices.append([self.x + i, self.y + wave_height, self.z + j])
                if i > 0 and j > 0:
                    self.faces.append(
                        (i * self.depth + j, (i - 1) * self.depth + j, (i - 1) * self.depth + j - 1))
                    self.faces.append(
                        (i * self.depth + j, (i - 1) * self.depth + j - 1, i * self.depth + j - 1))
    
    def draw(self):
        super().draw()
        self.update()

class Raindrop:
    def __init__(self):
        self.x = random.uniform(-100, 100)
        self.y = random.uniform(-100, 100)
        self.z = random.uniform(-100, 100)
        self.speed = random.uniform(0.05, 0.1)
        self.size = random.uniform(4.0, 5.0)

    def draw(self):
        use_texture("eau")
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glVertex3f(self.x, self.y, self.z)
        glEnd()

    def update(self):
        self.y -= self.speed
        if self.y < -1:
            self.y = 100

class Raindrops(Object):
    def __init__(self):
        self.raindrops = [Raindrop() for _ in range(RAINSIZE)]

    def draw(self):
        for drop in self.raindrops:
            drop.draw()
            drop.update()