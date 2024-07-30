# Desafio 46

Criando uma API REST simples com Flask

## Explicação

### Ferramentas Utilizadas

- `Flask`: Microframework do Python para criação de APIs web.
- `jsonify`: Função do Flask para converter dados em JSON.
- `request`: Objeto do Flask para acessar dados da requisição.

### Funções Principais

- `Flask(__name__)`: Cria uma aplicação Flask.
- `app.route()`: Define uma rota para a API.
- `jsonify()`: Converte dados em JSON para resposta.

## Resultado

```py
from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [
    {'id': 1, 'nome': 'Item 1', 'descricao': 'Descrição do Item 1'},
    {'id': 2, 'nome': 'Item 2', 'descricao': 'Descrição do Item 2'},
]

@app.route('/api/itens', methods=['GET'])
def obter_itens():
    return jsonify(dados)

@app.route('/api/itens/<int:item_id>', methods=['GET'])
def obter_item(item_id):
    item = next((item for item in dados if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'mensagem': 'Item não encontrado'}), 404

@app.route('/api/itens', methods=['POST'])
def adicionar_item():
    novo_item = request.get_json()
    dados.append(novo_item)
    return jsonify(novo_item), 201

@app.route('/api/itens/<int:item_id>', methods=['PUT'])
def atualizar_item(item_id):
    item = next((item for item in dados if item['id'] == item_id), None)
    if item:
        dados.remove(item)
        atualizado = request.get_json()
        dados.append(atualizado)
        return jsonify(atualizado)
    return jsonify({'mensagem': 'Item não encontrado'}), 404

@app.route('/api/itens/<int:item_id>', methods=['DELETE'])
def deletar_item(item_id):
    item = next((item for item in dados if item['id'] == item_id), None)
    if item:
        dados.remove(item)
        return jsonify({'mensagem': 'Item deletado'})
    return jsonify({'mensagem': 'Item não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)