# Desafio 75

Trabalhando com APIs GraphQL usando `requests`

## Explicação

### Ferramentas Utilizadas

- `requests`: Biblioteca para fazer requisições HTTP.

### Funções Principais

- `requests.post(url, headers, json)`: Envia uma requisição HTTP POST.

## Resultado

```py
import requests

url = "https://api.github.com/graphql"
token = "seu_token_aqui"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

query = """
{
  viewer {
    login
    name
  }
}
"""

response = requests.post(url, headers=headers, json={"query": query})

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")