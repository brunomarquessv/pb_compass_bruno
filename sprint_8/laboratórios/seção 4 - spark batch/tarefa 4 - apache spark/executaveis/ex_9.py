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


df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)

# 7) utilizando sparksql repetindo o processo do ex_6 registrando tambem uma tabela temporaria "pessoas"
df_nomes.createOrReplaceTempView("pessoas")
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_select_sql.select("Nomes", "AnoNascimento").show(10, truncate=False)

# 8) utilizando o metodo select do dataframe df_nomes, realizar contagem da quantidade de pessoas que pertencem
# a geração millenais (nascidos entre 1980 - 1994)

millenials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print("Millenials:", millenials)
#retorno esperado: Millenials: 2275087

# 9) repetindo o processo acima utilizando SparkSQL
millenials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
millenials = millenials_sql.collect()[0][0]
print("Contador Millenials com SQL:", millenials)
#retorno esperado: Contador Millenials com SQL: 2275087
