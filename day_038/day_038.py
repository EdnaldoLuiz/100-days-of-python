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
    # Configura o pool de processos
    numero_de_processos = 4
    pool = mp.Pool(processes=numero_de_processos)

    # Envia tarefas para o pool e coleta os resultados
    entrada = range(10)
    time.sleep(0.5)
    print(f"Enviando tarefas para o pool com {numero_de_processos} processos...")
    resultados = pool.map(tarefa, entrada)

    # Fecha o pool e aguarda todos os processos terminarem
    pool.close()
    pool.join()

    print(f"Resultados finais: {resultados}")