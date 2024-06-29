# Desafio 16

Validando e-mails e números de telefone com `re`

## Explicação

### Ferramentas Utilizadas

- `re`: Biblioteca padrão do Python para operações com expressões regulares.

### Funções Principais

- `re.match()`: Verifica se a expressão regular corresponde ao início da string.

### Padrões Utilizados

- E-mail: `^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$`
- Telefone: `^\(?[1-9]{2}\)? ?9?[0-9]{4}-?[0-9]{4}$`

## Resultado

```py
import re 

email = 'contatoednaldoluiz@gmail.com'

padrao = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$'

if re.match(padrao, email):
    print('E-mail válido!')
else:
    print('E-mail inválido!')

telefone = '1199999-9999'

padrao = r'^\(?[1-9]{2}\)? ?9?[0-9]{4}-?[0-9]{4}$'

if re.match(padrao, telefone):
    print('Número de telefone válido!')
else:
    print('Número de telefone inválido')