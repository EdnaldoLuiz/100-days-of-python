dicionarios = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Pedro', 'idade': 30}
]

print(sorted(dicionarios, key=lambda x: x['idade']))

print(sorted(dicionarios, key=lambda x: x['nome']))

