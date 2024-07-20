# Desafio 36

Trabalhando com Threads para tarefas paralelas simples

## Explicação

### Ferramentas Utilizadas

- `threading`: Biblioteca padrão do Python para criar e gerenciar threads.

### Funções Principais

- `threading.Thread()`: Cria uma nova thread.
- `thread.start()`: Inicia a execução da thread.
- `thread.join()`: Espera a conclusão da thread.

## Resultado

```py
import threading
import time

def tarefa(nome, tempo):
    print(f"Thread {nome} iniciada")
    time.sleep(tempo)
    print(f"Thread {nome} finalizada")

# Criando threads
thread1 = threading.Thread(target=tarefa, args=("A", 2))
thread2 = threading.Thread(target=tarefa, args=("B", 3))

# Iniciando threads
thread1.start()
thread2.start()

# Esperando a conclusão das threads
thread1.join()
thread2.join()

print("Todas as threads foram finalizadas")