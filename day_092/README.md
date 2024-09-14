# Desafio 92

Processando grandes volumes de dados com PySpark

## Explicação

### Ferramentas Utilizadas

- `pyspark.sql.SparkSession`: Biblioteca para criação de sessões Spark.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `SparkSession.builder.appName()`: Cria uma sessão Spark.
- `spark.read.csv()`: Lê um arquivo CSV em um DataFrame Spark.
- `df.filter()`: Filtra os dados do DataFrame.
- `df.groupBy().avg()`: Calcula a média de uma coluna.

## Resultado

```py
from pyspark.sql import SparkSession
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
large_dataset_path = os.path.join(assets_dir, 'large_dataset.csv')
result_path = os.path.join(assets_dir, 'resultado_filtrado.csv')

# Cria uma sessão Spark
spark = SparkSession.builder.appName("Processamento de Dados com PySpark").getOrCreate()

# Lê o arquivo CSV em um DataFrame Spark
df = spark.read.csv(large_dataset_path, header=True, inferSchema=True)

# Filtra os dados do DataFrame
df_filtrado = df.filter(df['valor'] > 100)

# Calcula a média da coluna 'valor'
media_valor = df_filtrado.groupBy().avg('valor').collect()[0][0]
print(f"Média da coluna 'valor': {media_valor}")

# Salva o DataFrame filtrado em um novo arquivo CSV
df_filtrado.write.csv(result_path, header=True)

# Encerra a sessão Spark
spark.stop()
```