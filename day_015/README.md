# Desafio 15

Manipulando arquivos de texto com `os` e `open`

## Explicação

### Ferramentas Utilizadas

- `os`: Biblioteca padrão do Python para interações com o sistema operacional.
- `open()`: Função padrão do Python para abrir arquivos.

### Funções Principais

- `os.path.join()`: Junta componentes de caminho de forma inteligente.
- `os.path.abspath()`: Retorna o caminho absoluto.
- `open()`: Abre um arquivo e retorna um objeto de arquivo.
- `file.read()`: Lê o conteúdo completo de um arquivo.
- `file.readlines()`: Lê todas as linhas de um arquivo e retorna uma lista.
- `file.write()`: Escreve uma string em um arquivo.

## Resultado

```py
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(base_dir, 'assets', 'arquivo.txt')

with open(arquivo, 'r') as file:
    conteudo = file.read()
    print(conteudo)

with open(arquivo, 'r') as file:
    linhas = file.readlines()
    for linha in linhas:
        print(linha)

arquivo = os.path.join(base_dir, 'assets', 'arquivo_vazio.txt')

with open(arquivo, 'w', encoding='utf-8') as file:
    file.write('Olá, mundo!\n')
    file.write('Python é uma linguagem de programação poderosa.\n')