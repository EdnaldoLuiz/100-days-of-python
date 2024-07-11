import http.server as server

def run(server_class=server.HTTPServer, handler_class=server.BaseHTTPRequestHandler):
    print('Servidor rodando em http://localhost:8000 no navegador.')
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()