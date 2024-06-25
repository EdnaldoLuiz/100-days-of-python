def gerador():
    for i in range(10):
        yield i

g = gerador()

print(next(g))  # Saída: 0
print(next(g))  # Saída: 1
print(next(g))  # Saída: 2