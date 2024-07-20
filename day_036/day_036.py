import threading

def tarefa(identificador):
    """
    Função executada por cada thread.
    Exibe o ID da thread e realiza uma tarefa simples.
    """
    tid = threading.get_ident()
    resultado = identificador ** 2 
    print(f"Thread ID {tid}: identificador {identificador}, resultado {resultado}")
    return resultado

if __name__ == '__main__':

    numero_de_threads = 4
    threads = []

    entrada = range(10)
    print(f"Enviando tarefas para as threads com {numero_de_threads} threads...")
    for i in entrada:
        thread = threading.Thread(target=tarefa, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todas as threads terminaram.")
    print("Fim do programa.")
