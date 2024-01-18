import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def set_light():
    # Activer l'éclairage et la source de lumière 0
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Définir les propriétés de la source de lumière 0
    light_position = [-20, 20, 40, 0.0]  # Position de la source de lumière
    light_ambient = [0.5, 0.5, 0.5, 1.0]  # Couleur ambiante de la lumière
    light_diffuse = [1.0, 1.0, 1.0, 1.0]  # Couleur diffuse de la lumière
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Couleur spéculaire de la lumière

    # Définir les propriétés de la source de lumière 0
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Définir la couleur ambiante globale de la lumière
    global_ambient = [0.5, 0.5, 0.5, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
