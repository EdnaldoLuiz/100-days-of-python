# Desafio 72

Construindo gráficos interativos com Bokeh

## Explicação

### Ferramentas Utilizadas

- `bokeh.plotting`: Biblioteca para criação de gráficos interativos.
- `bokeh.palettes`: Paletas de cores para gráficos.
- `bokeh.models`: Modelos para personalização de gráficos.
- `bokeh.layouts`: Layouts para organizar gráficos.

### Funções Principais

- `bp.figure()`: Cria uma nova figura para o gráfico.
- `fig.vbar()`: Adiciona um gráfico de barras verticais à figura.
- `fig.line()`: Adiciona um gráfico de linhas à figura.
- `bp.show()`: Exibe o gráfico.

## Resultado

```py
import bokeh.plotting as bp
import bokeh.palettes as bpl
import bokeh.models as bm
import bokeh.layouts as bl
import os

x = [1, 2, 3, 4, 5]
y_barras = [2, 3, 5, 7, 11]
y_linhas = [1, 4, 6, 8, 10]

fig = bp.figure(
    title="Gráfico de Barras e Linhas com Bokeh",
    x_axis_label="Eixo X",
    y_axis_label="Eixo Y",
    width=800,
    height=400
)

# Adiciona um gráfico de barras
fig.vbar(x=x, top=y_barras, width=0.5, color=bpl.Category10[5][0], legend_label="Barras")

# Adiciona um gráfico de linhas
fig.line(x=x, y=y_linhas, line_width=2, color=bpl.Category10[5][1], legend_label="Linhas")

# Exibe o gráfico
bp.show(fig)