# Desafio 31

Criando funções recursivas para calcular fatorial e sequência de Fibonacci

## Explicação

### Ferramentas Utilizadas

- Funções recursivas: Funções que chamam a si mesmas para resolver um problema.

### Funções Principais

- `fatorial(n)`: Calcula o fatorial de um número inteiro `n`.
- `fibonacci(n)`: Calcula o n-ésimo termo da sequência de Fibonacci.

## Resultado

```py
def fatorial(n):
    """
    Calcula o fatorial de um número inteiro n.
    """
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)