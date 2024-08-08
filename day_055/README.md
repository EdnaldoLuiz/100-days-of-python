# Desafio 55

Lidando com operações de ponto flutuante com precisão

## Explicação

### Ferramentas Utilizadas

- `decimal`: Biblioteca padrão do Python para operações de ponto flutuante com precisão.

### Funções Principais

- `decimal.getcontext().prec`: Define a precisão global para operações decimais.
- `decimal.Decimal()`: Cria um número decimal com precisão especificada.

## Resultado

```py
import decimal

# Define a precisão global para operações decimais
decimal.getcontext().prec = 4

# Cria números decimais com precisão especificada
numero_1 = decimal.Decimal('1.1')
numero_2 = decimal.Decimal('2.2')
resultado = numero_1 + numero_2
print(resultado)

numero_3 = decimal.Decimal('3.3536')
resultado = numero_1 + numero_3
print(resultado)