# Desafio 48

Gerando números aleatórios para simulações e testes

## Explicação

### Ferramentas Utilizadas

- `random`: Biblioteca padrão do Python para geração de números aleatórios.

### Funções Principais

- `random.random()`: Gera um número de ponto flutuante aleatório entre 0 e 1.
- `random.randint(a, b)`: Gera um número inteiro aleatório entre `a` e `b`.
- `random.randrange(start, stop, step)`: Gera um número inteiro aleatório entre `start` e `stop` com um passo `step`.
- `random.shuffle(lista)`: Embaralha a lista.

## Resultado

```py
import random

# Gera um número de ponto flutuante aleatório entre 0 e 1
numero = random.random()
print(numero)

# Gera um número inteiro aleatório entre 0 e 100
numero = random.randint(0, 100)
print(numero)

# Gera um número inteiro aleatório entre 0 e 100 com passo 5
numero = random.randrange(0, 100, 5)
print(numero)

# Embaralha a lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print(lista)