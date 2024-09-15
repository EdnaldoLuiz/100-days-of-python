import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interativo com Dash"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Category A', 'value': 'A'},
            {'label': 'Category B', 'value': 'B'},
            {'label': 'Category C', 'value': 'C'},
            {'label': 'Category D', 'value': 'D'}
        ],
        value='A'
    ),
    dcc.Graph(id='bar-graph')
])

@app.callback(
    Output('bar-graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.bar(filtered_df, x='Category', y='Values', title=f'Valores da Categoria {selected_category}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)