import pathlib

# Cria um objeto Path para o diretório atual

diretorio_atual = pathlib.Path('.')
print(diretorio_atual)

# Cria um objeto Path para um diretório específico

diretorio = pathlib.Path('/tmp')
print(diretorio)

# Cria um objeto Path para um arquivo específico

arquivo = pathlib.Path('/tmp/arquivo.txt')
print(arquivo)

# Verifica se um diretório ou arquivo existe

print(diretorio.exists())