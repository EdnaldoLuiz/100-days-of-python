# Desafio 27

Criando um servidor HTTP básico com Python

## Explicação

### Ferramentas Utilizadas

- `http.server`: Biblioteca padrão do Python para criar servidores HTTP.

### Funções Principais

- `server.HTTPServer`: Classe para criar um servidor HTTP.
- `server.BaseHTTPRequestHandler`: Classe base para manipular requisições HTTP.
- `httpd.serve_forever()`: Inicia o servidor e o mantém em execução.

## Resultado

```py
import http.server as server

def run(server_class=server.HTTPServer, handler_class=server.BaseHTTPRequestHandler):
    print('Servidor rodando em http://localhost:8000 no navegador.')
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()