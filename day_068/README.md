# Desafio 68

Criando um simulador de dados para APIs fictícias

## Explicação

### Ferramentas Utilizadas

- `Faker`: Biblioteca para geração de dados fictícios.

### Funções Principais

- `Faker()`: Cria um objeto Faker para geração de dados.
- `faker.name()`: Gera um nome fictício.
- `faker.address()`: Gera um endereço fictício.
- `faker.cpf()`: Gera um CPF fictício.
- `faker.phone_number()`: Gera um número de telefone fictício.

## Resultado

```py
from faker import Faker

faker = Faker('pt_BR')

nome = faker.name()
print(f"Nome: {nome}")

endereco = faker.address()
print(f"Endereço: {endereco}")

cpf = faker.cpf()
print(f"CPF: {cpf}")

telefone = faker.phone_number()
print(f"Telefone: {telefone}")