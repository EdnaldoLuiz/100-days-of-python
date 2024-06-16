# Desafio 3

Removendo itens de uma lista com base em uma condição

## Explicação

### Ferramentas Utilizadas

- `list`: Estrutura de dados padrão do Python para armazenar uma sequência de elementos.

### Funções Principais

- `list.remove()`: Remove o primeiro item da lista cujo valor é igual ao valor especificado.
- `list.append()`: Adiciona um item ao final da lista.
- `list.clear()`: Remove todos os itens da lista.

## Resultado

```py
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    if i % 2 == 0:
        print(f'{i} é par, remove da lista')
        lista.remove(i)

print(f"Lista de números ímpares: {lista}")

lista.clear()

for i in range(1, 11):
    if i % 2 != 0:
        lista.append(i)

print(f"Lista de números ímpares: {lista}")