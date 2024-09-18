# Desafio 96

Integrando e consumindo APIs de terceiros com OAuth2

## Explicação

### Ferramentas Utilizadas

- `requests`: Biblioteca para fazer requisições HTTP.
- `requests_oauthlib`: Biblioteca para autenticação OAuth.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `OAuth2Session()`: Cria uma sessão OAuth2.
- `oauth.fetch_token()`: Obtém um token de acesso OAuth2.

## Resultado

```python
import os
import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# Obtém as credenciais do cliente a partir das variáveis de ambiente
client_id = os.getenv('GITHUB_CLIENT_ID')
client_secret = os.getenv('GITHUB_CLIENT_SECRET')

# URL para obter o token de acesso
token_url = 'https://github.com/login/oauth/access_token'

# Cria um cliente OAuth2
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Obtém o token de acesso
token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

# Define a URL da API que será consumida
api_url = 'https://api.github.com/user'

# Faz uma requisição GET para a API usando o token de acesso
response = oauth.get(api_url)

# Exibe a resposta da API
print(response.json())
```