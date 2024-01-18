import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from shapes import *

# Fonction pour dessiner un buisson
def create_bush(x, y, z, width=1, height=1, depth=1, num_leaves=50):
    leaf_size = 0.85
    bush = [(x + random.uniform(0, width),
             y + random.uniform(0, height),
             z + random.uniform(0, depth)) for _ in range(num_leaves)]

    # Dessiner chaque feuille du buisson
    for leaf in bush:
        shapes.append(Cube(leaf[0], leaf[1], leaf[2], width=leaf_size,
                      height=leaf_size, depth=leaf_size, textures=["herbe"]))


# Fonction pour dessiner un arbre
def create_tree(x, y, z, width=3, height=4):
    # Dessiner le tronc de l'arbre
    shapes.append(Cylinder(x, y, z, radius=width/4,
                  height=height, textures=["tronc"]))

    # Dessiner le buisson au sommet de l'arbre
    use_texture("herbe")
    create_bush(x - width/2, y + height*4/5, z - width/2,
                width=width, height=height/2, depth=width)


# Fonction pour dessiner une maison
def create_house(x, y, z, width=8, height=4, depth=4):
    # Dessiner les murs de la maison
    shapes.append(Cube(x, y, z, width, height, depth, textures=["mur"]))
    # Dessiner le toit de la maison
    shapes.append(HouseRoof(x, y + height, z, width,
                  height/2, depth, textures=["toit"]))
    # Dessiner la porte de la maison
    shapes.append(Cube(x + width/2 - width/12, y, z + depth,
                       width=width/6, height=height*3/4, depth=0.1, textures=["bois"]))
    # Dessiner les fenêtres de la maison
    shapes.append(Cube(x + width*3/4, y + height/3, z + depth,
                       width=height/3, height=height/3, depth=0.01, textures=["fenetre"]))
    shapes.append(Cube(x + width/4 - height/3, y + height/3, z + depth,
                       width=height/3, height=height/3, depth=0.01, textures=["fenetre"]))
    # Dessiner la cheminée de la maison
    shapes.append(Cube(x + width/2 - width/12, y + height, z + depth/2,
                  width=width/12, height=height*2/3, depth=width/12, textures=["briques"]))


# Fonction pour dessiner l'environnement
def create_surroundings(x=-100, y=0, z=-100, width=200, depth=200, height=200):
    # Dessiner un cube pour représenter l'environnement
    shapes.append(Cube(x, y, z, width, height, depth, textures=[
                  "ciel-jour", "ciel-jour", "ciel-jour", "ciel-jour", "ciel-jour", "mur"]))


# Fonction pour dessiner une piscine
def create_pool(x, y, z, width=10, depth=10):
    # Dessiner les bords de la piscine
    for i in range(-width//2, width//2 + 1):
        shapes.append(Cube(x + i, y, z - depth//2, width=1,
                      height=1, depth=1, textures=["carrelage"]))
        shapes.append(Cube(x + i, y, z + depth//2, width=1,
                      height=1, depth=1, textures=["carrelage"]))
        shapes.append(Cube(x - width//2, y, z + i, width=1,
                      height=1, depth=1, textures=["carrelage"]))
        shapes.append(Cube(x + width//2, y, z + i, width=1,
                      height=1, depth=1, textures=["carrelage"]))
    # Dessiner les vagues à la surface de la piscine
    shapes.append(Wave(x - width//2 + 1, y + 0.3, z - depth//2 + 1, width=width,
                  depth=depth, amplitude=0.1, frequency=0.5, textures=["eau"]))


# Fonction pour dessiner une table
def create_table(x=0, y=-50, z=0, width=2, height=2, length=2):
    # Dessiner le plateau de la table
    shapes.append(Cube(x, y+height*9/10, z, width,
                  height/10, length, textures=["bois"]))
    # Dessiner les pieds de la table
    shapes.append(Cube(x, y, z, width/10, height,
                  length/10, textures=["bois"]))
    shapes.append(Cube(x, y, z+length*9/10, width/10,
                  height, length/10, textures=["bois"]))
    shapes.append(Cube(x+width*9/10, y, z, width/10,
                  height, length/10, textures=["bois"]))
    shapes.append(Cube(x+width*9/10, y, z+length*9/10, width /
                  10, height, length/10, textures=["bois"]))


# Fonction pour dessiner une route
def create_road(x=0, y=0, z=0, width=10, depth=10):
    # Dessiner la route
    shapes.append(Cube(x, y, z, width, 0.1, depth, textures=["route"]))


# Fonction pour dessiner un village
def create_village(x=0, y=0, z=0, number_per_line=3, space_between=10):
    # Dessiner les maisons du village
    for i in range(number_per_line):
        for j in range(number_per_line):
            create_house(x + i*space_between, y, z + j*space_between)
    # Dessiner la route du village
    create_road(x, y, z, (number_per_line-1)*space_between +
                8, (number_per_line-1)*space_between+4)


# Fonction pour dessiner une forêt
def create_forest(x=0, y=0, z=0, number_per_line=2, space_between=7):
    # Dessiner les arbres de la forêt
    for i in range(number_per_line):
        for j in range(number_per_line):
            create_tree(x + i*space_between, y, z + j*space_between)
    # Dessiner une table au centre de la forêt
    create_table(x + (number_per_line-1)*space_between/2-1,
                 y, z + (number_per_line-1)*space_between/2-1)

def create_raindrops():
    shapes.append(Raindrops())

def create_objects():
    create_surroundings()
    create_pool(-10, 0, 20)
    create_village(0, 0, 0)
    create_forest(-12, 0, 5)
    create_raindrops()