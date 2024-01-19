## Lab AWS - Glue

### Etapas:

#### Etapas 1 e 2 
1. Leitura do arquivo csv;
2. Print do schema do dataframe gerado pela leitura do arquivo csv;
<br>
- [.json etapas 1 e 2](../lab_aws_glue/json/etapa_1_2_lab_glue.json)
```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# etapa 1: ler o arquivo .csv 
# etapa 2: criando o dynamic_frame de acordo com o código exemplo
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

# print do schema
print()
dynamic_frame.printSchema()

# salvar como .json
data_frame = dynamic_frame.toDF()
DataFrameWriter(data_frame).mode('append').json(target_path)

job.commit()
```

#### Etapa 3 
3. Alterar a caixa de valores da coluna nome para MAIÚSCULO
- [.json da etapa 3](../lab_aws_glue/json/etapa_3_maiusculo_lab_glue.json)

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter, functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# leitura do arquivo .csv
# criação do dynamic_frame
dynamic_frame = glueContext.create_dynamic_frame.from_options(
  "s3",
  {"paths": [source_file]},
  "csv",
  {"withHeader": True, "separator": ","}
)

# visualização dos dados da coluna nome em maiusculo
apply_upper = ApplyMapping.apply(frame=dynamic_frame, mappings=[("nome", "string", "nome", "string")])
resolvechoice = ResolveChoice.apply(frame=apply_upper, choice="make_cols")
data_frame = resolvechoice.toDF()
data_frame = data_frame.withColumn("nome", F.upper(data_frame["nome"]))

# salvar como .json
DataFrameWriter(data_frame).mode('append').json(target_path)

job.commit()
```

#### Etapa 4
4. Imprimir a contagem de linhas presentes no dataframe
[.json da etapa 4](../lab_aws_glue/json/etapa_4_contagem.json)
```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter, functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# leitura do arquivo .csv
# criação do dynamic_frame
dynamic_frame = glueContext.create_dynamic_frame.from_options(
  "s3",
  {"paths": [source_file]},
  "csv",
  {"withHeader": True, "separator": ","}
)

data_frame = dynamic_frame.toDF()

# contador de linhas
numero_linhas = dynamic_frame.count()
row = Row("numero de linhas")
dynamic_frame_linhas = spark.createDataFrame([row(numero_linhas)])

# salvar como .json
DataFrameWriter(data_frame).mode('append').json(target_path)

job.commit()
```

#### Etapa 5
5.Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo
[.json da etapa 5]()
```

```

#### Criação do crawler
![](../lab_aws_glue/assets/Screenshot%202024-01-19%20135251.png)
![](../lab_aws_glue/assets/Screenshot%202024-01-19%20135715.png)