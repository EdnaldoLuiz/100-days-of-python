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
    else:
        return jsonify({'mensagem': 'Item não encontrado'}), 404

@app.route('/api/itens', methods=['POST'])
def adicionar_item():
    novo_item = request.get_json()
    dados.append(novo_item)
    return jsonify(novo_item), 201

@app.route('/api/itens/<int:item_id>', methods=['DELETE'])
def deletar_item(item_id):
    item = next((item for item in dados if item['id'] == item_id), None)
    if item:
        dados.remove(item)
        return jsonify({'mensagem': 'Item deletado'})
    else:
        return jsonify({'mensagem': 'Item não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)