# Desafio 70

Criando animações básicas com Matplotlib

## Explicação

### Ferramentas Utilizadas

- `matplotlib.pyplot`: Biblioteca para criação de gráficos em Python.
- `matplotlib.animation`: Módulo para criação de animações.

### Funções Principais

- `FuncAnimation()`: Cria uma animação chamando uma função repetidamente.

## Resultado

```py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.set_title("Animação de Gráfico de Linhas")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

xdata, ydata = [], []
ln, = ax.plot([], [], linestyle='-', color='b', label='Linha 1')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(frame ** 2)
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                              init_func=init, blit=True)

plt.legend()
plt.show()