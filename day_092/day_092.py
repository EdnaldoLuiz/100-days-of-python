from pyspark.sql import SparkSession
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
large_dataset_path = os.path.join(assets_dir, 'large_dataset.csv')
result_path = os.path.join(assets_dir, 'resultado_filtrado.csv')

spark = SparkSession.builder.appName("Processamento de Dados com PySpark").getOrCreate()

df = spark.read.csv(large_dataset_path, header=True, inferSchema=True)

df_filtrado = df.filter(df['valor'] > 100)

media_valor = df_filtrado.groupBy().avg('valor').collect()[0][0]
print(f"Média da coluna 'valor': {media_valor}")

df_filtrado.write.csv(result_path, header=True)

spark.stop()