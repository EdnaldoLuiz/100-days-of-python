import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_path = librosa.example('trumpet')
y, sr = librosa.load(audio_path)

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
S_dB = librosa.power_to_db(S, ref=np.max)

zero_crossings = librosa.feature.zero_crossing_rate(y)

spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Mel')
plt.tight_layout()

plt.figure(figsize=(10, 4))
plt.semilogy(zero_crossings.T, label='Taxa de cruzamento por zero')
plt.xlabel('Quadros')
plt.ylabel('Taxa de cruzamento por zero')
plt.title('Taxa de cruzamento por zero')
plt.tight_layout()

plt.figure(figsize=(10, 4))
plt.semilogy(spectral_centroid.T, label='Espectro de frequência')
plt.xlabel('Quadros')
plt.ylabel('Hz')
plt.title('Espectro de frequência')
plt.tight_layout()

plt.show()