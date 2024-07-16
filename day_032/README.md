# Desafio 32

Trabalhando com argumentos variáveis (`*args` e `**kwargs`) em funções

## Explicação

### Ferramentas Utilizadas

- `*args`: Permite passar um número variável de argumentos posicionais para uma função.
- `**kwargs`: Permite passar um número variável de argumentos nomeados para uma função.

### Funções Principais

- `*args`: Captura todos os argumentos posicionais como uma tupla.
- `**kwargs`: Captura todos os argumentos nomeados como um dicionário.

## Resultado

```py
def funcao(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

funcao(1, 2, 3, a=4, b=5)