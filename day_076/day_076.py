import os
from PIL import Image, ImageDraw, ImageFont

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
image_path = os.path.join(assets_dir, "fundo.jpg")

imagem_fundo = Image.open(os.path.join(base_dir, image_path))

desenho = ImageDraw.Draw(imagem_fundo)
texto = "Python é incrível!"
fonte = ImageFont.truetype(os.path.join(base_dir, "arial.ttf"), 36)
posicao = (50, 50)
cor = (255, 255, 255)
desenho.text(posicao, texto, font=fonte, fill=cor)

imagem_fundo.show()