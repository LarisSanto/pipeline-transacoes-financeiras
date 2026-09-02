# Importando as ferramentas do PySpark e do SQLite nativo para conversar com o banco de dados.
from pyspark.sql import SparkSession
import sqlite3
import os

print("Acordando o Spark para a etapa de carga no banco...")

# 1- Criando a sessão do Spark (sem precisar baixar drivers da web).
spark = SparkSession.builder \
    .appName("CargaBancoTransacoes") \
    .getOrCreate()

print("Spark pronto!")

# 2- Lendo os dados tratados.
pasta_origem = "dados_tratados"
print(f"Lendo os dados limpos da pasta: {pasta_origem}")

df_limpo = spark.read.parquet(pasta_origem)

print(f"Total de linhas limpas prontas para ir para o banco: {df_limpo.count()}")

print("Convertendo os dados para o formato que o banco adora...")

# Transformando o DataFrame do Spark em um DataFrame do Pandas.
df_pandas = df_limpo.toPandas()

# 3- Conectando e salvando no banco de dados relacional (SQLite).
nome_banco = "transacoes.db"
nome_tabela = "tabela_transacoes"

print(f"Gravando os dados na tabela '{nome_tabela}' dentro do banco de dados relacional...")

# Conectando ao banco SQLite local (ele cria o arquivo transacoes.db sozinho se não existir)
conexao = sqlite3.connect(nome_banco)

# Salvando os dados do Pandas direto para a tabela do SQLite
df_pandas.to_sql(nome_tabela, conexao, if_exists="replace", index=False)

# Fechando a conexão com carinho
conexao.close()

print("Processo concluído! Nossas transações financeiras agora estão salvas no banco de dados relacional e prontas para consultas.")

