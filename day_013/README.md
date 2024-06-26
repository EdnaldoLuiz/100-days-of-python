# Desafio 13

Manipulando arquivos JSON com `json`

## Explicação

### Ferramentas Utilizadas

- `json`: Biblioteca padrão do Python para manipulação de dados JSON.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `json.load()`: Lê um arquivo JSON e o converte em um objeto Python.
- `json.dump()`: Converte um objeto Python em JSON e grava em um arquivo.
- `os.path.join()`: Junta componentes de caminho de forma inteligente.
- `os.path.abspath()`: Retorna o caminho absoluto.

## Resultado

```py
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