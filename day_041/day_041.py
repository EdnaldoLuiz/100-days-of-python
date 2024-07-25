import plotly.graph_objects as go
import plotly.express as px

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

def criar_grafico_pizza():
    fig = px.pie(values=[10, 20, 30, 40], names=['A', 'B', 'C', 'D'], title='Gráfico de Pizza')
    fig.show()

if __name__ == '__main__':
    criar_grafico_barras()
    criar_grafico_dispersao()
    criar_grafico_linhas()
    criar_grafico_pizza()