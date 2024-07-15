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

if __name__ == '__main__':
    numero = 5
    print(f"Fatorial de {numero}: {fatorial(numero)}")

    n = 10
    print(f"Sequência de Fibonacci de {n} termos:")
    for i in range(n):
        print(fibonacci(i), end=' ')
    print()