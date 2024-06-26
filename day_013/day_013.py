import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
arquivo_leitura = os.path.join(base_dir, 'assets', 'pessoas.json')
arquivo_escrita = os.path.join(base_dir, 'assets', 'pessoas_copia.json')

with open(arquivo_leitura, 'r') as file:
    data = json.load(file)

print(data)

data['age'] = 25

with open(arquivo_escrita, 'w') as file:
    json.dump(data, file)

with open(arquivo_escrita, 'r') as file:
    data = json.load(file)

print(data)