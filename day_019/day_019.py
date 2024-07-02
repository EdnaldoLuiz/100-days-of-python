from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
foto_de_gato = os.path.join(base_dir, 'assets', 'gato.jpg')

imagem = Image.open(foto_de_gato)
imagem.show()