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