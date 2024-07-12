# Desafio 28

Lidando com exceções personalizadas em Python

## Explicação

### Ferramentas Utilizadas

- `Exception`: Classe base para todas as exceções em Python.

### Funções Principais

- `class MyError(Exception)`: Define uma exceção personalizada.
- `__init__()`: Inicializa a exceção com um valor.
- `__str__()`: Define a representação em string da exceção.
- `raise`: Lança uma exceção.
- `try`/`except`: Bloco para capturar e lidar com exceções.

## Resultado

```py
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('Uma exceção ocorreu: ', e.value)