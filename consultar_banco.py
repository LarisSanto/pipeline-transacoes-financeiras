import sqlite3

# Conectando ao nosso banco de dados relacional
conexao = sqlite3.connect("transacoes.db")
cursor = conexao.cursor()

print("Fazendo uma consulta rápida no banco de dados...")

# Buscando as 5 primeiras transações salvas na nossa tabela
cursor.execute("SELECT * FROM tabela_transacoes LIMIT 5;")
linhas = cursor.fetchall()

print("Aqui estão as primeiras transações salvas:")
for linha in linhas:
    print(linha)

# Fechando a conexão
conexao.close()