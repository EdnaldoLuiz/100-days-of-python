# Desafio 76

Gerando imagens com texto sobreposto usando Pillow

## Explicação

### Ferramentas Utilizadas

- `Pillow`: Biblioteca para manipulação de imagens.

### Funções Principais

- `Image.open()`: Abre uma imagem.
- `ImageDraw.Draw()`: Cria um objeto de desenho.
- `ImageFont.truetype()`: Carrega uma fonte TrueType.
- `desenho.text()`: Desenha texto na imagem.

## Resultado

```py
import os
from PIL import Image, ImageDraw, ImageFont

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
image_path = os.path.join(assets_dir, "fundo.jpg")

# Abre a imagem de fundo
imagem_fundo = Image.open(image_path)

# Cria um objeto de desenho
desenho = ImageDraw.Draw(imagem_fundo)

# Define o texto, fonte, posição e cor
texto = "Python é incrível!"
fonte = ImageFont.truetype(os.path.join(base_dir, "arial.ttf"), 36)
posicao = (50, 50)
cor = (255, 255, 255)

# Desenha o texto na imagem
desenho.text(posicao, texto, font=fonte, fill=cor)

# Salva a imagem resultante
imagem_fundo.save(os.path.join(assets_dir, "imagem_com_texto.jpg"))

# Exibe a imagem resultante
imagem_fundo.show()