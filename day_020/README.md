# Desafio 20

Criando gráficos simples com `matplotlib`

## Explicação

### Ferramentas Utilizadas

- `matplotlib.pyplot`: Biblioteca para criação de gráficos em Python.

### Funções Principais

- `plt.plot()`: Cria um gráfico de linha.

## Resultado

```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.show()