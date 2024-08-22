# Desafio 69

Explorando bancos de dados não relacionais com MongoDB

## Explicação

### Ferramentas Utilizadas

- `pymongo`: Biblioteca para interagir com MongoDB em Python.

### Funções Principais

- `MongoClient()`: Cria uma conexão com o servidor MongoDB.
- `cliente['banco_de_dados']`: Acessa um banco de dados.
- `banco_de_dados['colecao']`: Acessa uma coleção dentro do banco de dados.
- `colecao.insert_one()`: Insere um documento na coleção.
- `colecao.insert_many()`: Insere múltiplos documentos na coleção.
- `colecao.find()`: Recupera documentos da coleção.
- `colecao.update_one()`: Atualiza um documento na coleção.
- `colecao.delete_one()`: Remove um documento da coleção.

## Resultado

```py
import pymongo

# Conecta ao servidor MongoDB
cliente = pymongo.MongoClient('mongodb://localhost:27017/')
banco_de_dados = cliente['exemplo']
colecao = banco_de_dados['pessoas']

# Cria documentos
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

# Insere documentos na coleção
colecao.insert_one(documento_1)
colecao.insert_one(documento_2)

# Cria e insere múltiplos documentos na coleção
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

# Recupera e exibe documentos da coleção
for documento in colecao.find():
    print(documento)

# Atualiza um documento na coleção
filtro = {'nome': 'Alice'}
novo_valor = {'$set': {'cidade': 'Campinas'}}
colecao.update_one(filtro, novo_valor)

# Remove um documento da coleção
filtro = {'nome': 'Bob'}
colecao.delete_one(filtro)

# Recupera e exibe documentos atualizados da coleção
for documento in colecao.find():
    print(documento)