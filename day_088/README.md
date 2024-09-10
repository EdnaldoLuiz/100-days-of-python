# Desafio 88

Processando vídeos e capturando frames com OpenCV

## Explicação

### Ferramentas Utilizadas

- `cv2`: Biblioteca OpenCV para processamento de imagens e vídeos.
- `requests`: Biblioteca para fazer requisições HTTP.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `cv2.VideoCapture()`: Abre um arquivo de vídeo.
- `cap.read()`: Lê um frame do vídeo.
- `cv2.imwrite()`: Salva uma imagem em um arquivo.

## Resultado

```py
import cv2
import os
import requests

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
video_path = os.path.join(assets_dir, 'video.mp4')
video_url = "https://cdn.pixabay.com/video/2021/02/17/65438-514139134_large.mp4"

# Baixa o vídeo se não existir
if not os.path.exists(video_path):
    print("Baixando o vídeo...")
    response = requests.get(video_url, stream=True)
    with open(video_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Salva cada frame como uma imagem
    frame_path = os.path.join(assets_dir, f'frame_{frame_count}.jpg')
    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()
print(f"Processamento concluído. {frame_count} frames capturados.")