import cv2
import os
import requests

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
video_path = os.path.join(assets_dir, 'video.mp4')
video_url = "https://cdn.pixabay.com/video/2021/02/17/65438-514139134_large.mp4"

if not os.path.exists(video_path):
    print("Baixando o vídeo...")
    response = requests.get(video_url, stream=True)
    with open(video_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print("Vídeo baixado com sucesso.")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

frames_dir = os.path.join(assets_dir, 'frames')
os.makedirs(frames_dir, exist_ok=True)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao ler o frame.")
        break

    if frame_count % 30 == 0:
        frame_path = os.path.join(frames_dir, f"frame_{frame_count}.jpg")
        success = cv2.imwrite(frame_path, frame)
        if success:
            print(f"Frame {frame_count} capturado e salvo em {frame_path}")
        else:
            print(f"Erro ao salvar o frame {frame_count}")

    frame_count += 1

cap.release()
print("Processamento do vídeo concluído.")