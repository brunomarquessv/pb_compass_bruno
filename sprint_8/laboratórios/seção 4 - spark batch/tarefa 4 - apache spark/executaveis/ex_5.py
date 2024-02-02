from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when
from pyspark.sql.functions import expr

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

caminho_arquivo = "pb-compass-bruno\\sprint_8\\laboratórios\\seção 4 - spark batch\\tarefa 4 - apache spark\\nomes_aleatorios.txt"

df_nomes = spark.read.text(caminho_arquivo)

df_nomes = df_nomes.withColumnRenamed("value", "Nomes")
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental").when(rand() < 0.67, "Médio").otherwise("Superior"))

df_nomes = df_nomes.withColumn("País", expr("array('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela')[int(rand() * 13)]"))

#adicionado coluna ano de nascimento
df_nomes = df_nomes.withColumn("AnoNascimento", expr("int(rand() * (2010 - 1945 + 1)) + 1945"))

df_nomes.show(10)