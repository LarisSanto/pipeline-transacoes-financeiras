# Pipeline de Engenharia de Dados: Transações Financeiras



<img width="3365" height="974" alt="eng" src="https://github.com/user-attachments/assets/869239e6-5dda-40f7-8359-1859d2dac4b8" />

### O Problema de Negócio
Empresas financeiras recebem diariamente grandes volumes de arquivos brutos (como CSVs de transações) que chegam sem validação, contêm inconsistências (valores nulos ou erros) e estão espalhados, inviabilizando análises rápidas e seguras.

### A Solução Proposta
Construção de um pipeline de dados automatizado utilizando PySpark para simular a extração, tratamento rigoroso e limpeza de um volume massivo de dados transacionais, salvando o resultado particionado em formato otimizado e carregando-o em um banco de dados relacional (SQLite / Data Warehouse local).

### Tecnologias Utilizadas
* Python
* Apache Spark (PySpark)
* Pandas & SQLite
* Git & GitHub

### Estrutura do Projeto
* `dados_brutos/`: Arquivos CSV originais extraídos do Kaggle.
* `dados_tratados/`: Dados limpos e salvos em formato profissional Parquet.
* `transacoes.db`: Banco de dados relacional final (Data Warehouse).
* `processar_dados.py`: Script de limpeza e transformação com PySpark.
* `carregar_banco.py`: Script de carga para o banco de dados.

### Como Executar
1. Instale as dependências: `pip install pyspark pandas kagglehub`
2. Baixe os dados: `python baixar_dados.py`
3. Execute a limpeza: `python processar_dados.py`
4. Carregue no banco: `python carregar_banco.py`

<br>



