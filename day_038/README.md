# Desafio 38

Lidando com tempo e atrasos usando `time.sleep`

## Explicação

### Ferramentas Utilizadas

- `time`: Biblioteca padrão do Python para manipulação de tempo.

### Funções Principais

- `time.sleep(segundos)`: Suspende a execução do programa pelo número de segundos especificado.

## Resultado

```py
import multiprocessing as mp
import os
import time

def tarefa(identificador):
    """
    Função executada por cada processo no pool.
    Exibe o ID do processo e realiza uma tarefa simples.
    """
    pid = os.getpid()
    resultado = identificador ** 2 
    print(f"Processo ID {pid}: identificador {identificador}, resultado {resultado}")
    time.sleep(3)
    return resultado

if __name__ == '__main__':
    numero_de_processos = 4
    pool = mp.Pool(processes=numero_de_processos)

    entrada = range(10)
    print(f"Enviando tarefas para o pool com {numero_de_processos} processos...")
    resultados = pool.map(tarefa, entrada)

    pool.close()
    pool.join()

    print(f"Resultados finais: {resultados}")