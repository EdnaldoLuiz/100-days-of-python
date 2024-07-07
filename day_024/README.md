# Desafio 24

Criando e manipulando dataclasses para representar objetos

## Explicação

### Ferramentas Utilizadas

- `dataclasses`: Biblioteca padrão do Python para criar classes de dados.

### Funções Principais

- `@dataclass`: Decorador para definir uma dataclass.
- Atributos da dataclass: Definidos com tipo e nome.

## Resultado

```py
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cidade: str

p1 = Pessoa('João', 25, 'São Paulo')
p2 = Pessoa('Maria', 20, 'Rio de Janeiro')
p3 = Pessoa('Pedro', 30, 'Curitiba')

print(p1)
print(p2)
print(p3)