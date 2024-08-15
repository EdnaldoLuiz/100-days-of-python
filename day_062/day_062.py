def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

def main(alvo):
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    resultado = busca_binaria(lista, alvo)

    if resultado != -1:
        print(f"Elemento {alvo} encontrado no índice {resultado}.")
    else:
        print(f"Elemento {alvo} não encontrado na lista.")

if __name__ == "__main__":
    main(int(input("Digite o elemento a ser buscado: ")))