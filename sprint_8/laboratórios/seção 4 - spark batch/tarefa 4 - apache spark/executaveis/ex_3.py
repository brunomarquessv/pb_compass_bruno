from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "pb-compass-bruno\\sprint_8\\laboratórios\\seção 4 - spark batch\\tarefa 4 - apache spark\\nomes_aleatorios.txt"

df_nomes = spark.read.text(caminho_arquivo)

df_nomes = df_nomes.withColumnRenamed("value", "Nomes")
#adicionado coluna de escolaridade 
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental").when(rand() < 0.67, "Médio").otherwise("Superior"))

df_nomes.show(10)
