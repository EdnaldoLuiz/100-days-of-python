s = frozenset([1, 2, 3, 4, 5])
x = set([1, 2, 3, 4, 5])

print("O conjunto imutável é : ", s)

# As operações abaixo não são permitidas em frozenset
# s.add(6)
# s.remove(1)
# s.update([10, 11])
# s.discard(5)
# s.clear()

# Operações permitidas em frozenset
novo_set = s.union(x)
novo_set.add(6)