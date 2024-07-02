# Desafio 19

Manipulando imagens com `PIL`

## Explicação

### Ferramentas Utilizadas

- `PIL`: Biblioteca Python Imaging Library para abrir, manipular e salvar arquivos de imagem.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `Image.open()`: Abre um arquivo de imagem.
- `imagem.show()`: Exibe a imagem.

## Resultado

```py
from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
foto_de_gato = os.path.join(base_dir, 'assets', 'gato.jpg')

imagem = Image.open(foto_de_gato)
imagem.show()