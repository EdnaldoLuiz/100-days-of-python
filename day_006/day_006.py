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
