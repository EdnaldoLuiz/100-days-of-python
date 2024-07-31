import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Idade': [24, 32, 45, 27, 19],
    'Sexo': ['F', 'M', 'M', 'M', 'M']
}

df = pd.DataFrame(dados)

print(df)

dados = [
    ('Alice', 24, 'F'),
    ('Bob', 32, 'M'),
    ('Charlie', 45, 'M'),
    ('David', 27, 'M'),
    ('Edward', 19, 'M')
]

df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Sexo'])

print(df)