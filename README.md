<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="Apache Spark">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</p>

<h1 align="center">Pipeline de Engenharia de Dados: Transações Financeiras</h1>


<p align="center">
  <b>Construção de uma esteira ETL ponta a ponta para processamento, transformação e persistência de dados financeiros.</b>
</p>

<br>
<p align="center">
  
### Visão Geral do Projeto
</p>
Este projeto simula um ambiente corporativo de engenharia de dados, focado em coletar informações brutas, realizar uma faxina rigorosa e estruturar dados transacionais para o consumo analítico seguro.

* O Problema: Empresas financeiras lidam diariamente com volumes massivos de arquivos CSV que chegam sem validação, contêm nulos ou inconsistências e estão descentralizados, impedindo análises ágeis.
* A Solução: Um pipeline automatizado em PySpark que executa o tratamento em larga escala, armazena os dados processados em formato otimizado (Parquet) e realiza a carga final em um banco relacional (SQLite / Data Warehouse local).

<br>

### Arquitetura do Pipeline

<p align="center">
  <img src="https://github.com/user-attachments/assets/869239e6-5dda-40f7-8359-1859d2dac4b8" alt="Arquitetura do Pipeline" width="850px">
</p>

---



---

### Tecnologias Utilizadas

* Linguagem: Python 3.12
* Processamento: Apache Spark (PySpark)
* Manipulação: Pandas
* Armazenamento: Apache Parquet & SQLite
* Controle de Versão: Git & GitHub

---

### Estrutura do Repositório

```text
pipeline-transacoes-financeiras/
│
├── dados_brutos/          # Arquivos CSV originais extraídos do Kaggle
├── dados_tratados/        # Dados limpos salvos em formato Parquet particionado
├── img/                   # Recursos visuais e diagramas
├── baixar_dados.py        # Automação para download do dataset
├── processar_dados.py     # Script PySpark de limpeza e transformação
├── carregar_banco.py      # Script de carga e persistência no banco SQLite
├── consultar_banco.py     # Script de validação via consultas SQL
├── transacoes.db          # Banco de dados relacional final (Data Warehouse)
└── README.md              # Documentação oficial do projeto
```

### Como Executar

1. Instale as dependências: `pip install pyspark pandas kagglehub`
2. Baixe os dados: `python baixar_dados.py`
3. Execute a limpeza: `python processar_dados.py`
4. Carregue no banco: `python carregar_banco.py`

