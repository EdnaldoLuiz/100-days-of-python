# Desafio 66

Implementando um algoritmo de ordenação (ex: bubble sort)

## Explicação

### Ferramentas Utilizadas

- Algoritmo de ordenação: Método para organizar elementos em uma sequência ordenada.

### Funções Principais

- `bubble_sort(array)`: Implementa o algoritmo de ordenação Bubble Sort.

## Resultado

```py
array = [5, 3, 8, 6, 2, 7, 1, 4]

def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubble_sort(array)
print(array)