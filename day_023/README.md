# Desafio 23

Ordenando listas de dicionários com `sorted` e lambdas

## Explicação

### Ferramentas Utilizadas

- `sorted()`: Função padrão do Python para ordenar iteráveis.
- `lambda`: Função anônima usada para definir a chave de ordenação.

### Funções Principais

- `sorted(iterável, key=lambda x: x['chave'])`: Ordena a lista de dicionários com base na chave especificada.

## Resultado

```py
dicionarios = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Pedro', 'idade': 30}
]

print(sorted(dicionarios, key=lambda x: x['idade']))
print(sorted(dicionarios, key=lambda x: x['nome']))