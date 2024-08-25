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
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

# Gráfico de Barras
fig.vbar(x=x, top=y_barras, width=0.5, color=bpl.Category10[5], legend_label="Barras")

# Gráfico de Linhas
fig.line(x, y_linhas, line_width=2, color="green", legend_label="Linhas")
fig.circle(x, y_linhas, size=8, color="green", legend_label="Pontos")

hover = bm.HoverTool()
hover.tooltips = [
    ("Índice", "$index"),
    ("(X, Y)", "($x, $y)"),
]
fig.add_tools(hover)

fig.legend.location = "top_left"
fig.legend.title = "Legenda"
fig.title.text_font_size = "16pt"
fig.xaxis.axis_label_text_font_size = "12pt"
fig.yaxis.axis_label_text_font_size="12pt"

label = bm.Label(x=3, y=7, text="Ponto de Interesse", text_font_size="10pt", text_color="red")
fig.add_layout(label)

layout = bl.column(fig)

base_path = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_path, 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_file_path = os.path.join(assets_dir, 'grafico.html')

bp.output_file(output_file_path)
bp.save(layout)

print(f"Gráfico salvo em: {output_file_path}")

bp.show(layout)