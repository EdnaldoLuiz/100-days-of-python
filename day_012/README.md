# Desafio 12

Utilizando geradores em Python

## Explicação

### Ferramentas Utilizadas

- `yield`: Palavra-chave do Python para criar geradores.

### Funções Principais

- `yield`: Pausa a função e retorna um valor, permitindo a retomada da execução.
- `next()`: Retorna o próximo valor do gerador.

## Resultado

```py
def gerador():
    for i in range(10):
        yield i

g = gerador()

print(next(g))  # Saída: 0
print(next(g))  # Saída: 1
print(next(g))  # Saída: 2