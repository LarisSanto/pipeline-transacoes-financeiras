# Importando as ferramentas do PySpark consegui trabalhar.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, current_timestamp
from pyspark.sql.types import DoubleType

print("Acordando o Spark para começar o trabalho...")

# 1- Criando a sessão do Spark e ligando o motor do robo.
spark = SparkSession.builder \
    .appName("PipelineTransacoesFinanceiras") \
    .getOrCreate()

print("Spark pronto para a ação!")

# 2- Encontrado e lendo os arquivos e dizendo aonde está o arquivo que baixamos.
import os 
pasta_dados = "dados_brutos"
arquivo_csv = ""

for f in os.listdir(pasta_dados):
    if f.endswith(".csv"):
        arquivo_csv = os.path.join(pasta_dados, f)
        break

print(f"Lendo o aquivo bruto: {arquivo_csv}")

# Spark lê o arquivo CSV. O header=True avisa que a primeira linha tem o nome das colunas
df_bruto = spark.read.option("header", "true").option("inferSchema", "true").csv(arquivo_csv)

print("Quantidade de linhas bagunçadas recebidas: {df_bruto.count()}")

# 3- Fazendo a limpeza e tratamento dos dados. 
print("Iniciando a limpeza e tratamento...")

df_bruto.printSchema()

df_limpo = df_bruto \
    .na.drop(subset=[df_bruto.columns[0]]) \
    .withColumn("data_processamento", current_timestamp())

print("Processo concluido, dados limpos e organizados.")

# 4- Salvando os resultados em partições.
pasta_destino = "dados_tratados"

print("Salvando os dados organizados na pasta: {pasta_destino}")

df_limpo.write \
    .mode("overwrite") \
    .parquet(pasta_destino)

print("Processo finalizado com sucesso!")



















