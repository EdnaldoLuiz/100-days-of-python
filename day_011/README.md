# Desafio 11

Manipulando listas e compreensões de listas

## Explicação

### Ferramentas Utilizadas

- `list`: Estrutura de dados padrão do Python para armazenar sequências de elementos.
- Compreensão de listas: Sintaxe concisa para criar listas a partir de iteráveis.

### Funções Principais

- Indexação de listas: `lista[indice]` para acessar elementos.
- Compreensão de listas: `[expressão for item in iterável]` para criar listas.

## Resultado

```py
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista[0])  # Saída: [1, 2, 3]
print(lista[1][0])  # Saída: 4

lista = [i for i in range(10)]

print(lista)  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]