# Desafio 35

Usando decorators para modificar o comportamento de funções

## Explicação

### Ferramentas Utilizadas

- Decorators: Funções que modificam o comportamento de outras funções.

### Funções Principais

- `@decorator`: Aplica o decorator à função.
- `wrapper()`: Função interna que envolve a função original.

## Resultado

```py
def decorator(funcao):
    def wrapper():
        print("Antes da função decorada")
        funcao()
        print("Depois da função decorada")
    return wrapper

@decorator
def funcao_decorada():
    n = 2 + 2
    print(f"Resultado: {n}")

funcao_decorada()
```