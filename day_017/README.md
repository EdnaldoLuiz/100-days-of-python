# Desafio 17

Fazendo requisições HTTP com `requests`

## Explicação

### Ferramentas Utilizadas

- `requests`: Biblioteca popular do Python para fazer requisições HTTP.

### Funções Principais

- `requests.get()`: Faz uma requisição GET para a URL especificada.
- `response.status_code`: Retorna o código de status da resposta HTTP.
- `response.json()`: Converte a resposta JSON em um objeto Python.

## Resultado

```py
import requests

response = requests.get('https://api.github.com/users/EdnaldoLuiz')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")