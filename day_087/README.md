# Desafio 87

Criando um servidor HTTP simples com manipulação de requisições GET e POST

## Explicação

### Ferramentas Utilizadas

- `http.server`: Biblioteca padrão do Python para criação de servidores HTTP.
- `urllib.parse`: Biblioteca padrão do Python para manipulação de URLs.

### Funções Principais

- `SimpleHTTPRequestHandler`: Classe base para manipulação de requisições HTTP.
- `do_GET()`: Manipula requisições GET.
- `do_POST()`: Manipula requisições POST.

## Resultado

```py
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET recebido!</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = urlparse.parse_qs(post_data.decode('utf-8'))
        response = f"<html><body><h1>POST recebido!</h1><p>Data: {parsed_data}</p></body></html>"
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()