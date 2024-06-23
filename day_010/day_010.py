dicionario_desordenado = { 'a': 8, 'b': 6, 'c': 3, 'd': 4, 'e': 1 }

print(dicionario_desordenado) 

dicionario_ordenado = dict(sorted(dicionario_desordenado.items(), key=lambda item: item[1]))

print(dicionario_ordenado)