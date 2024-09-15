# Desafio 93

Criando dashboards interativos com Dash

## Explicação

### Ferramentas Utilizadas

- `dash`: Biblioteca para criação de dashboards interativos.
- `dash_core_components`: Componentes centrais do Dash.
- `dash_html_components`: Componentes HTML do Dash.
- `plotly.express`: Biblioteca para criação de gráficos interativos.
- `pandas`: Biblioteca para manipulação de dados.

### Funções Principais

- `dash.Dash()`: Cria uma aplicação Dash.
- `html.Div()`: Cria um contêiner HTML.
- `dcc.Graph()`: Cria um componente de gráfico.
- `dcc.Dropdown()`: Cria um componente de dropdown.
- `app.callback()`: Define uma função de callback para atualizar o gráfico.

## Resultado

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# Cria a aplicação Dash
app = dash.Dash(__name__)

# Define o layout da aplicação
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': cat, 'value': cat} for cat in df['Category']],
        value='A'
    ),
    dcc.Graph(id='graph')
])

# Define a função de callback para atualizar o gráfico
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.bar(filtered_df, x='Category', y='Values', title=f'Valores da Categoria {selected_category}')
    return fig

# Executa a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)