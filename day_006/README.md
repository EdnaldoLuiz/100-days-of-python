# Desafio 6

Manipulando arquivos CSV com `pandas`

## Explicação

### Ferramentas Utilizadas

- `pandas`: Biblioteca poderosa para análise e manipulação de dados.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.
- `pathlib`: Biblioteca padrão do Python para manipulação de caminhos de arquivos.

### Funções Principais

- `pd.read_csv()`: Lê um arquivo CSV e o converte em um DataFrame.
- `df.to_csv()`: Escreve um DataFrame em um arquivo CSV.
- `os.makedirs()`: Cria diretórios recursivamente.
- `os.path.join()`: Junta componentes de caminho de forma inteligente.
- `os.path.abspath()`: Retorna o caminho absoluto.

## Resultado

```py
from pathlib import Path
import pandas as pd
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
assets_dir = os.path.join(base_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
csv_leitura = os.path.join(assets_dir, 'leitura.csv')
csv_escrita = os.path.join(assets_dir, 'escrita.csv')

df = pd.read_csv(csv_leitura, sep=';')
print(f"Lendo o arquivo CSV:\n{df}")

df.to_csv(csv_escrita, index=False)
print(f"Gravando o arquivo CSV:\n{df}")