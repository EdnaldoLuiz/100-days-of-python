# Desafio 89

Explorando visualizações avançadas com Altair

## Explicação

### Ferramentas Utilizadas

- `altair`: Biblioteca para criação de visualizações declarativas.
- `pandas`: Biblioteca para manipulação de dados.
- `numpy`: Biblioteca para computação numérica eficiente.

### Funções Principais

- `alt.Chart()`: Cria um gráfico Altair.
- `mark_circle()`: Define o tipo de marcação como círculo.
- `encode()`: Define as codificações para os eixos e outras propriedades visuais.

## Resultado

```py
import altair as alt
import pandas as pd
import numpy as np

# Gera dados aleatórios
np.random.seed(40)
n = 100
df = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'category': np.random.choice(['A', 'B', 'C'], n)
})

# Cria um gráfico de dispersão
scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x='x',
    y='y',
    color='category',
    tooltip=['x', 'y', 'category']
).interactive()

# Exibe o gráfico
scatter_plot.show()
```