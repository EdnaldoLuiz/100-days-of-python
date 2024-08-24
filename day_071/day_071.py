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
    print(f"Thread {identificador} terminou.")

if __name__ == '__main__':
    numero_de_threads = 4
    pool = [threading.Thread(target=tarefa, args=(i,)) for i in range(numero_de_threads)]

    print(f"Iniciando {numero_de_threads} threads...")
    for thread in pool:
        thread.start()

    for thread in pool:
        thread.join()

    print(f"Todas as threads terminaram. Valor final do contador: {contador}")