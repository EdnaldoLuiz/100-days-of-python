import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'ebdb'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Criar uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS exemplo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL
)
""")

cursor.execute("""
INSERT INTO exemplo (nome, idade) VALUES (%s, %s)
""", ('Alice', 30))
conn.commit()

cursor.execute("SELECT * FROM exemplo")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

cursor.execute("""
UPDATE exemplo SET idade = %s WHERE nome = %s
""", (31, 'Alice'))
conn.commit()

cursor.execute("""
DELETE FROM exemplo WHERE nome = %s
""", ('Alice',))
conn.commit()

cursor.close()
conn.close()