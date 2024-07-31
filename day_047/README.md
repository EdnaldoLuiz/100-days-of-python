# Desafio 47

Explorando dados tabulares com a biblioteca `pandas`

## Explicação

### Ferramentas Utilizadas

- `pandas`: Biblioteca poderosa para análise e manipulação de dados tabulares.

### Funções Principais

- `pd.DataFrame()`: Cria um DataFrame a partir de dados.
- `df.head()`: Exibe as primeiras linhas do DataFrame.
- `df.describe()`: Gera estatísticas descritivas do DataFrame.
- `df.info()`: Exibe um resumo das informações do DataFrame.

## Resultado

```py
import pandas as pd

# Criando um DataFrame
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [28, 22, 35, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte']
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibindo estatísticas descritivas do DataFrame
print(df.describe())

# Exibindo um resumo das informações do DataFrame
print(df.info())