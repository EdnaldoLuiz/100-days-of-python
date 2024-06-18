# Desafio 5

Filtrando um dicionário com compreensão de dicionário

## Explicação

### Ferramentas Utilizadas

- `dict`: Estrutura de dados padrão do Python para armazenar pares chave-valor.
- Compreensão de dicionário: Sintaxe concisa para criar dicionários a partir de iteráveis.

### Funções Principais

- `dicionario.items()`: Retorna uma nova visão dos pares chave-valor do dicionário.
- Compreensão de dicionário: `{chave: valor for chave, valor in iterável if condição}`

## Resultado

```py
dicionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

filtrado = { chave: valor for chave, valor in dicionario.items() if valor > 2 }

print(filtrado)