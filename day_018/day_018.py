import zipfile
import gzip
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
arquivo = os.path.join(assets_dir, 'arquivo.txt')
utf8 = 'utf-8'

# Compressão de arquivos

with open(arquivo, 'w', encoding=utf8) as file:
    file.write('Olá, mundo!')

# Compressão com gzip
gzip_arquivo = os.path.join(assets_dir, 'arquivo.txt.gz')
with open(arquivo, 'rb') as file:
    with gzip.open(gzip_arquivo, 'wb') as zipped_file:
        zipped_file.writelines(file)

# Compressão com zipfile
zip_arquivo = os.path.join(assets_dir, 'arquivo.zip')
with open(arquivo, 'rb') as file:
    with zipfile.ZipFile(zip_arquivo, 'w') as zipped_file:
        zipped_file.write(arquivo, os.path.basename(arquivo))

# Descompressão de arquivos

# Descompressão com zipfile
with zipfile.ZipFile(zip_arquivo, 'r') as zipped_file:
    zipped_file.extractall(assets_dir)

# Descompressão com gzip
with gzip.open(gzip_arquivo, 'rb') as zipped_file:
    with open(arquivo, 'wb') as file:
        file.writelines(zipped_file)