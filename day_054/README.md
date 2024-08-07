# Desafio 54

Gerenciando threads e filas simultaneamente com `queue`

## Explicação

### Ferramentas Utilizadas

- `threading`: Biblioteca padrão do Python para criação e gerenciamento de threads.
- `queue`: Biblioteca padrão do Python para criação e gerenciamento de filas.

### Funções Principais

- `threading.Thread()`: Cria uma nova thread.
- `thread.start()`: Inicia a execução da thread.
- `thread.join()`: Espera a conclusão da thread.
- `queue.Queue()`: Cria uma nova fila.
- `queue.put()`: Adiciona um item à fila.
- `queue.get()`: Remove e retorna um item da fila.

## Resultado

```py
import threading
import queue

def tarefa(q):
    """
    Função executada por cada thread.
    Exibe o ID da thread e realiza uma tarefa simples.
    """
    while not q.empty():
        identificador = q.get()
        tid = threading.get_ident()
        resultado = identificador ** 2
        print(f"Thread ID {tid}: identificador {identificador}, resultado {resultado}")
        q.task_done()

if __name__ == '__main__':
    q = queue.Queue()
    numero_de_threads = 4

    # Adiciona tarefas à fila
    for i in range(10):
        q.put(i)

    # Cria e inicia threads
    threads = []
    for _ in range(numero_de_threads):
        thread = threading.Thread(target=tarefa, args=(q,))
        thread.start()
        threads.append(thread)

    # Espera a conclusão de todas as tarefas
    q.join()

    # Espera a conclusão de todas as threads
    for thread in threads:
        thread.join()

    print("Todas as tarefas foram concluídas")