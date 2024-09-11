import altair as alt
import pandas as pd
import numpy as np

np.random.seed(40)
n = 100
df = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'category': np.random.choice(['A', 'B', 'C'], n)
})

scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x='x',
    y='y',
    color='category',
    tooltip=['x', 'y', 'category']
).interactive().properties(
    title='Gráfico de Dispersão'
)

scatter_plot