# Importation des modules nécessaires
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from objects import *
from light import *
from fog import *
from rain import *

# Variables pour la position et la direction de la caméra
x = 0
y = 0
z = 0
angle_h = 0
angle_v = 0

# Fonction pour décrire la scène
def render_Scene():
    draw_scene()
    generate_rain()

# Fonction pour l'animation
def idle():
    time.sleep(0.01)
    glutPostRedisplay()

# Fonction pour redimensionner la fenêtre
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(35, 20, 45, 0, 0, 0, 0, 1, 0)

# Fonction pour afficher la scène
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(x, y, z, x + math.sin(angle_h), y + math.sin(angle_v), z - math.cos(angle_h), 0, 1, 0)
    render_Scene()
    glPopMatrix()
    glutSwapBuffers()

# Fonction pour gérer les touches du clavier
def keyboard(key, xx, yy):
    global x, y, z, angle_h, angle_v
    speed = 0.5
    if key == GLUT_KEY_F1:
        x += speed * math.sin(angle_h)
        y += speed * math.sin(angle_v)
        z -= speed * math.cos(angle_h)
    elif key == GLUT_KEY_F2:
        x -= speed * math.sin(angle_h)
        y -= speed * math.sin(angle_v)
        z += speed * math.cos(angle_h)
    elif key == GLUT_KEY_LEFT:
        angle_h -= speed
    elif key == GLUT_KEY_RIGHT:
        angle_h += speed
    elif key == GLUT_KEY_DOWN:
        angle_v -= speed
    elif key == GLUT_KEY_UP:
        angle_v += speed
    glutPostRedisplay()

# Fonction principale
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Village")
    load_textures()
    set_light()
    set_fog()
    draw_objects()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()
