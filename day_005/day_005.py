dicionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

filtrado = { chave: valor for chave, valor in dicionario.items() if valor > 2 }

print(filtrado)