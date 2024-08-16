# Desafio 63

Criando e manipulando um gráfico de dispersão com Seaborn

## Explicação

### Ferramentas Utilizadas

- `seaborn`: Biblioteca para visualização de dados baseada em Matplotlib.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `sns.load_dataset()`: Carrega um conjunto de dados de exemplo.
- `sns.scatterplot()`: Cria um gráfico de dispersão.
- `grafico.get_figure().savefig()`: Salva o gráfico em um arquivo.

## Resultado

```py
import seaborn as sns
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
image_path = os.path.join(assets_dir, "grafico_de_dispersao.png")

# Carrega o conjunto de dados de exemplo
dados = sns.load_dataset("tips")

print(dados.head())

# Cria um gráfico de dispersão
grafico = sns.scatterplot(x="total_bill", y="tip", data=dados)

# Salva o gráfico em um arquivo
grafico.get_figure().savefig(image_path)