# Desafio 60

Extraindo dados da web com BeautifulSoup para web scraping

## Explicação

### Ferramentas Utilizadas

- `requests`: Biblioteca para fazer requisições HTTP.
- `BeautifulSoup`: Biblioteca para extrair dados de arquivos HTML e XML.

### Funções Principais

- `requests.get(url)`: Faz uma requisição GET para a URL especificada.
- `BeautifulSoup(html, "html.parser")`: Cria um objeto BeautifulSoup para analisar o HTML.
- `soup.title`: Obtém a tag `<title>` do HTML.
- `soup.title.string`: Obtém o texto dentro da tag `<title>`.

## Resultado

```py
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup.title)
print(soup.title.string)