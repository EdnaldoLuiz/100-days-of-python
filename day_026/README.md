# Desafio 26

Criando e manipulando conjuntos imutáveis com `frozenset`

## Explicação

### Ferramentas Utilizadas

- `frozenset`: Estrutura de dados do Python para criar conjuntos imutáveis.
- `set`: Estrutura de dados do Python para criar conjuntos mutáveis.

### Funções Principais

- `frozenset()`: Cria um conjunto imutável.
- Métodos de `frozenset`: Não permite adição, remoção ou atualização de elementos.
- Métodos de `set`: Permite adição, remoção e atualização de elementos.

## Resultado

```py
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
print("Novo conjunto após união: ", novo_set)