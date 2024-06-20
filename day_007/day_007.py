conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(conjunto)

conjunto.add(11)
print(conjunto)

conjunto.remove(11)
print(conjunto)

print(1 in conjunto)

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {4, 5, 6, 7, 8}
uniao = conjunto_1.union(conjunto_2)

print(uniao)

intersecao = conjunto_1.intersection(conjunto_2)
print(intersecao)

diferenca = conjunto_1.difference(conjunto_2)
print(diferenca)

diferenca_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print(diferenca_simetrica)

print(conjunto_1.issubset(conjunto_2))

print(conjunto_1.issuperset(conjunto_2))

print(conjunto_1.isdisjoint(conjunto_2))

conjunto_vazio = set()
print(conjunto_vazio)