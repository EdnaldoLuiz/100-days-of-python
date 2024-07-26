# Desafio 42

Gerenciando arquivos e diretórios com a biblioteca `pathlib`

## Explicação

### Ferramentas Utilizadas

- `pathlib`: Biblioteca padrão do Python para manipulação de caminhos de arquivos e diretórios.

### Funções Principais

- `pathlib.Path()`: Cria um objeto Path.
- `Path('.')`: Representa o diretório atual.
- `Path('/caminho')`: Representa um caminho específico.

## Resultado

```py
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