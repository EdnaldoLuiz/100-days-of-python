# Desafio 79

Criando visualizações em 3D com Matplotlib

## Explicação

### Ferramentas Utilizadas

- `matplotlib.pyplot`: Biblioteca para criação de gráficos em Python.
- `numpy`: Biblioteca para computação numérica eficiente.

### Funções Principais

- `fig.add_subplot(111, projection='3d')`: Adiciona um subplot 3D à figura.
- `ax.scatter(x, y, z)`: Cria um gráfico de dispersão 3D.

## Resultado

```py
import matplotlib.pyplot as plt
import numpy as np

# Cria uma figura
fig = plt.figure()

# Adiciona um subplot 3D à figura
ax = fig.add_subplot(111, projection='3d')

# Gera dados aleatórios
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

# Cria um gráfico de dispersão 3D
ax.scatter(x, y, z)

# Exibe o gráfico
plt.show()