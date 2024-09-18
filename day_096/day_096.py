import os
import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

client_id = os.getenv('GITHUB_CLIENT_ID')
client_secret = os.getenv('GITHUB_CLIENT_SECRET')

token_url = 'https://github.com/login/oauth/access_token'

client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

api_url = 'https://api.github.com/user'
response = oauth.get(api_url)

if response.status_code == 200:
    user_data = response.json()
    print(f"Nome do usuário: {user_data['name']}")
    print(f"Login do usuário: {user_data['login']}")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)