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
    repositories(first: 5) {
      nodes {
        name
        description
        url
      }
    }
  }
}
"""

response = requests.post(url, json={'query': query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Dados recebidos da API GraphQL:")
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)