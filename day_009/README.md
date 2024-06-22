# Desafio 9

Utilizando `enum` para definir constantes

## Explicação

### Ferramentas Utilizadas

- `enum`: Biblioteca padrão do Python para criar enumeradores.

### Funções Principais

- `Enum`: Classe base para criar enumeradores.
- `Enum.value`: Retorna o valor associado a um membro do enumerador.
- `Enum()`: Construtor para comparar valores de enumeradores.
- Método de instância: `is_success()`, verifica se o status HTTP é de sucesso.

## Resultado

```py
from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0
    PENDING = 2

print(Status.ACTIVE)  
print(Status.ACTIVE.value)  

if Status.ACTIVE == Status(1):
    print("Status ativo!")

class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

    def is_success(self):
        return 200 <= self.value < 300

print(HttpStatus.OK.is_success()) 
print(HttpStatus.NOT_FOUND.is_success())