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

print(p1 == p2)
print(p1 == p1)

print(p1 == Pessoa('João', 25, 'São Paulo'))
print(p1 == Pessoa('João', 25, 'Curitiba'))
print(p1 == Pessoa('João', 30, 'São Paulo'))
