import requests

response = requests.get('https://api.github.com/users/EdnaldoLuiz')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")