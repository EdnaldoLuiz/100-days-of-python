# Desafio 83

Processando áudio e extraindo características com Librosa

## Explicação

### Ferramentas Utilizadas

- `librosa`: Biblioteca para análise de áudio.
- `matplotlib.pyplot`: Biblioteca para criação de gráficos em Python.
- `numpy`: Biblioteca para computação numérica eficiente.

### Funções Principais

- `librosa.load()`: Carrega um arquivo de áudio.
- `librosa.feature.melspectrogram()`: Calcula o espectrograma mel.
- `librosa.power_to_db()`: Converte uma escala de potência para decibéis.
- `librosa.feature.zero_crossing_rate()`: Calcula a taxa de cruzamento por zero.
- `librosa.feature.spectral_centroid()`: Calcula o centróide espectral.

## Resultado

```py
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Carrega um exemplo de áudio
audio_path = librosa.example('trumpet')
y, sr = librosa.load(audio_path)

# Calcula o espectrograma mel
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
S_dB = librosa.power_to_db(S, ref=np.max)

# Calcula a taxa de cruzamento por zero
zero_crossings = librosa.feature.zero_crossing_rate(y)

# Calcula o centróide espectral
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

# Exibe o espectrograma mel
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma Mel')
plt.tight_layout()
plt.show()

# Exibe a taxa de cruzamento por zero
plt.figure(figsize=(10, 4))
plt.plot(zero_crossings[0])
plt.title('Taxa de Cruzamento por Zero')
plt.tight_layout()
plt.show()

# Exibe o centróide espectral
plt.figure(figsize=(10, 4))
plt.semilogy(spectral_centroid.T, label='Centróide Espectral')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spectral_centroid.shape[-1]])
plt.legend(loc='upper right')
plt.title('Centróide Espectral')
plt.tight_layout()
plt.show()