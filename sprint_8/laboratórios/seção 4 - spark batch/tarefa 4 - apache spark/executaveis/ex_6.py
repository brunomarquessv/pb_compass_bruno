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

df_nomes = df_nomes.withColumn("AnoNascimento", expr("int(rand() * (2010 - 1945 + 1)) + 1945"))

# selecionando pessoas que nasceram no século vigente (21) e armazenando resultado em outro dataframe chamado df_select
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)

df_select.select("Nomes").show(10, truncate=False)

# imprimindo com as demais colunas (escolaridade, país e ano nascimento)
df_select.show(5)
