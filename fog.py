from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def set_fog():
    # Définition de la couleur du brouillard
    fog_color = [0.5, 0.5, 0.5, 0.2]
    
    # Activation du brouillard
    glEnable(GL_FOG)

    # Définition du mode de brouillard (linéaire)
    glFogi(GL_FOG_MODE, GL_LINEAR)

    # Définition de la couleur du brouillard
    glFogfv(GL_FOG_COLOR, fog_color)

    # Définition de la densité du brouillard
    glFogf(GL_FOG_DENSITY, 0.05)

    # Définition de l'indice de qualité du brouillard
    glHint(GL_FOG_HINT, GL_DONT_CARE)

    # Définition de la distance de début du brouillard
    glFogf(GL_FOG_START, 20.0)

    # Définition de la distance de fin du brouillard
    glFogf(GL_FOG_END, 100.0)
