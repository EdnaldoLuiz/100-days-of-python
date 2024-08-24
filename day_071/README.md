# Desafio 71

Trabalhando com variáveis globais em scripts multi-thread

## Explicação

### Ferramentas Utilizadas

- `threading`: Biblioteca padrão do Python para criação e gerenciamento de threads.
- `threading.Lock()`: Cria um bloqueio para garantir acesso exclusivo a uma variável compartilhada.

### Funções Principais

- `with lock`: Garante que a seção crítica seja executada por apenas uma thread de cada vez.

## Resultado

```py
import threading

contador = 0
lock = threading.Lock()

def tarefa(identificador):
    """
    Função executada por cada thread.
    Incrementa a variável global 'contador' de forma segura.
    """
    global contador
    for _ in range(1000):
        with lock:
            contador += 1

if __name__ == '__main__':
    threads = []
    numero_de_threads = 10

    # Cria e inicia threads
    for i in range(numero_de_threads):
        thread = threading.Thread(target=tarefa, args=(i,))
        thread.start()
        threads.append(thread)

    # Espera a conclusão de todas as threads
    for thread in threads:
        thread.join()

    print(f"Valor final do contador: {contador}")