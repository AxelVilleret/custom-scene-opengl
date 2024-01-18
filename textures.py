import os
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

textures = {}


def load_texture(filename):
    try:
        # Charger la texture
        image = Image.open(filename)
        image_data = np.array(list(image.getdata()), np.uint8)

        # Créer un objet texture
        id_textures = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, id_textures)

        # Définir les paramètres de la texture
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Charger l'image de texture dans l'objet texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height,
                     0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

        return id_textures  # Retourner l'ID de la texture
    except Exception as e:
        print(f"Échec du chargement de la texture {filename}: {e}")
        return None


def load_textures():
    global textures
    directory = "textures"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            path = os.path.join(directory, filename)
            texture_name = os.path.splitext(
                filename)[0]
            texture_id = load_texture(path)
            if texture_id is not None:
                textures[texture_name] = texture_id


def use_texture(texture_name):
    if texture_name in textures:
        glBindTexture(GL_TEXTURE_2D, textures[texture_name])
    else:
        print(f"Texture {texture_name} non trouvée")
