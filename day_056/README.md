# Desafio 56

Criando e verificando arquivos zip protegidos por senha

## Explicação

### Ferramentas Utilizadas

- `zipfile`: Biblioteca padrão do Python para manipulação de arquivos ZIP.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `zipfile.ZipFile()`: Cria ou abre um arquivo ZIP.
- `zipfile.ZipFile.write()`: Adiciona um arquivo ao ZIP.
- `zipfile.ZipFile.extractall()`: Extrai todos os arquivos do ZIP.

## Resultado

```py
import zipfile
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
file_1 = os.path.join(assets_dir, 'arquivo_1.txt')
file_2 = os.path.join(assets_dir, 'arquivo_2.txt')
zip_file = os.path.join(assets_dir, 'arquivo.zip')

os.makedirs(assets_dir, exist_ok=True)

def criar_zip_senha(arquivo_zip, arquivos, senha):
    """
    Cria um arquivo zip protegido por senha.
    """
    with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
    with zipfile.ZipFile(arquivo_zip) as zipf:
        zipf.setpassword(senha.encode())

def extrair_zip_senha(arquivo_zip, destino, senha):
    """
    Extrai um arquivo zip protegido por senha.
    """
    with zipfile.ZipFile(arquivo_zip) as zipf:
        zipf.extractall(path=destino, pwd=senha.encode())

# Criando arquivos de exemplo
with open(file_1, 'w') as f:
    f.write("Conteúdo do arquivo 1")
with open(file_2, 'w') as f:
    f.write("Conteúdo do arquivo 2")

# Criando arquivo zip protegido por senha
criar_zip_senha(zip_file, [file_1, file_2], 'senha123')

# Extraindo arquivo zip protegido por senha
extrair_zip_senha(zip_file, assets_dir, 'senha123')

print("Arquivos zip criados e extraídos com sucesso.")