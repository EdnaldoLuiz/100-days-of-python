# Desafio 40

Gerenciando variáveis de ambiente com `os.environ`

## Explicação

### Ferramentas Utilizadas

- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `os.environ`: Dicionário que contém as variáveis de ambiente.
- `os.environ.get()`: Obtém o valor de uma variável de ambiente.
- `os.environ['VAR'] = 'valor'`: Define uma variável de ambiente.
- `del os.environ['VAR']`: Remove uma variável de ambiente.

## Resultado

```py
import os

os.environ['MY_VARIABLE'] = 'some_value'

my_variable = os.environ.get('MY_VARIABLE')
print(f"MY_VARIABLE: {my_variable}")

if 'MY_VARIABLE' in os.environ:
    print("MY_VARIABLE está definida")

del os.environ['MY_VARIABLE']

my_variable = os.environ.get('MY_VARIABLE')
print(f"MY_VARIABLE após remoção: {my_variable}")