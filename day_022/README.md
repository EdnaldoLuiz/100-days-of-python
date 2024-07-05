# Desafio 22

Trabalhando com operadores personalizados para classes

## Explicação

### Ferramentas Utilizadas

- Classes e Objetos: Estrutura de dados para modelar entidades com atributos e métodos.
- Operadores personalizados: Métodos especiais para definir o comportamento de operadores.

### Funções Principais

- `__init__()`: Método inicializador para definir atributos da classe.
- `__str__()`: Método para definir a representação em string do objeto.
- `__add__()`: Método para definir o comportamento do operador `+`.

## Resultado

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)