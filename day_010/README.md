# Desafio 10

Ordenando um dicionário por valores

## Explicação

### Ferramentas Utilizadas

- `dict`: Estrutura de dados padrão do Python para armazenar pares chave-valor.
- `sorted()`: Função padrão do Python para ordenar iteráveis.

### Funções Principais

- `dict.items()`: Retorna uma nova visão dos pares chave-valor do dicionário.
- `sorted()`: Ordena os itens do dicionário com base em uma chave.
- `lambda`: Função anônima usada para definir a chave de ordenação.

## Resultado

```py
dicionario_desordenado = { 'a': 8, 'b': 6, 'c': 3, 'd': 4, 'e': 1 }

print(dicionario_desordenado) 

dicionario_ordenado = dict(sorted(dicionario_desordenado.items(), key=lambda item: item[1]))

print(dicionario_ordenado)