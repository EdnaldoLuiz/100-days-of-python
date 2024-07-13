# Desafio 29

Lendo e manipulando bancos de dados MySQL

## Explicação

### Ferramentas Utilizadas

- `mysql.connector`: Biblioteca para conectar e interagir com bancos de dados MySQL.

### Funções Principais

- `cursor.execute()`: Executa uma consulta SQL.
- `conn.commit()`: Confirma as alterações no banco de dados.
- `cursor.close()`: Fecha o cursor.
- `conn.close()`: Fecha a conexão com o banco de dados.

## Resultado

```py
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)

cursor = conn.cursor()

cursor.execute("""
DELETE FROM exemplo WHERE nome = %s
""", ('Alice',))
conn.commit()

cursor.close()
conn.close()
```