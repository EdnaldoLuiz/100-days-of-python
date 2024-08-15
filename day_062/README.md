# Desafio 62

Implementando um algoritmo de busca binária

## Explicação

### Ferramentas Utilizadas

- Algoritmo de busca binária: Método eficiente para encontrar um item em uma lista ordenada.

### Funções Principais

- `busca_binaria(lista, alvo)`: Implementa a busca binária para encontrar o índice do `alvo` na `lista`.

## Resultado

```py
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

# Exemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 7
resultado = busca_binaria(lista, alvo)
print(f"Elemento {alvo} encontrado no índice {resultado}")