from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "pb-compass-bruno\\sprint_8\\laboratórios\\seção 4 - spark batch\\tarefa 4 - apache spark\\nomes_aleatorios.txt"

df_nomes = spark.read.text(caminho_arquivo)
df_nomes.printSchema()

#ajustado o nome da coluna value para Nomes
df_nomes = df_nomes.withColumnRenamed("value", "Nomes")

df_nomes.show(10)