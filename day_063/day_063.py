import seaborn as sns
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
image_path = os.path.join(assets_dir, "grafico_de_dispersao.png")

dados = sns.load_dataset("tips")

print(dados.head())

grafico = sns.scatterplot(x="total_bill", y="tip", data=dados)
grafico.get_figure().savefig(image_path)

print(f"Gráfico salvo em {image_path}")