# Desafio 41

Criando e manipulando gráficos interativos com Plotly

## Explicação

### Ferramentas Utilizadas

- `plotly.graph_objects`: Biblioteca para criar gráficos interativos.
- `plotly.express`: Biblioteca para criar gráficos de forma simplificada.

### Funções Principais

- `go.Figure()`: Cria uma nova figura.
- `go.Bar()`: Cria um gráfico de barras.
- `go.Scatter()`: Cria um gráfico de dispersão ou linhas.
- `fig.update_layout()`: Atualiza o layout do gráfico.
- `fig.show()`: Exibe o gráfico.

## Resultado

```py
import plotly.graph_objects as go

def criar_grafico_barras():
    fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C', 'D', 'E'], y=[1, 2, 3, 4, 5])])
    fig.update_layout(title='Gráfico de Barras', xaxis_title='Categorias', yaxis_title='Valores')
    fig.show()

def criar_grafico_dispersao():
    fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], mode='markers'))
    fig.update_layout(title='Gráfico de Dispersão', xaxis_title='X', yaxis_title='Y')
    fig.show()

def criar_grafico_linhas():
    fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], mode='lines'))
    fig.update_layout(title='Gráfico de Linhas', xaxis_title='X', yaxis_title='Y')
    fig.show()

if __name__ == '__main__':
    criar_grafico_barras()
    criar_grafico_dispersao()
    criar_grafico_linhas()