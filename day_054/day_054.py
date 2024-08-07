import threading

def tarefa(identificador):
    """
    Função executada por cada thread.
    Exibe o ID da thread e realiza uma tarefa simples.
    """

    tid = threading.get_ident()
    resultado = identificador ** 2
    print(f"Thread ID {tid}: identificador {identificador}, resultado {resultado}")

if __name__ == '__main__':
    fila = []
    numero_de_threads = 4

    print(f"Iniciando {numero_de_threads} threads...")
    for i in range(numero_de_threads):
        thread = threading.Thread(target=tarefa, args=(i,))
        thread.start()
        fila.append(thread)

    for thread in fila:
        thread.join()

    print("Todas as threads terminaram.")