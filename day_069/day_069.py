import pymongo

cliente = pymongo.MongoClient('mongodb://localhost:27017/')
banco_de_dados = cliente['exemplo']
colecao = banco_de_dados['pessoas']

documento_1 = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo'
}

documento_2 = {
    'nome': 'Bob',
    'idade': 30,
    'cidade': 'Rio de Janeiro'
}

colecao.insert_one(documento_1)
colecao.insert_one(documento_2)

documentos = [
    {
        'nome': 'Charlie',
        'idade': 35,
        'cidade': 'Curitiba'
    },
    {
        'nome': 'David',
        'idade': 40,
        'cidade': 'Belo Horizonte'
    }
]

colecao.insert_many(documentos)

for documento in colecao.find():
    print(documento)

filtro = {'nome': 'Alice'}
novo_valor = {'$set': {'cidade': 'Campinas'}}
colecao.update_one(filtro, novo_valor)

filtro = {'nome': 'Bob'}
colecao.delete_one(filtro)