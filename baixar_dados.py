# Importando a biblioteca do Kaggle.
import kagglehub
import shutil
import os
print("Iniciando o download da base de dados de transações financeiras...")

# Aqui kagglehub vai baixar os dados e guardar em uma pasta secreta da nuvem.
caminho_baixado = kagglehub.dataset_download("mdshabbiralikhan/credit-card-fraud-detection-practice-dataset")

print(f"Dados baixados com sucesso na pasta temporária: {caminho_baixado}")

# Vamos criar uma pasta 'dados_brutos' no nosso projeto.
pasta_do_projeto = "dados_brutos"
os.makedirs(pasta_do_projeto, exist_ok=True)

# Vamos procurar o arquivo CSV dentro da pasta que o kaggle baixou e copiá-lo para a nossa pasta.
for arquivo in os.listdir(caminho_baixado):
    if arquivo.endswith(".csv"):
        origem = os.path.join(caminho_baixado, arquivo)
        destino = os.path.join(pasta_do_projeto, arquivo)
        
        # Copiando o arquivo para a nossa pasta do projeto.
        shutil.copy(origem, destino)
        print(f"Arquivo CSV copiado com sucesso para: {destino}")

print("Tudo pronto! Nosso arquivo de transações financeiras já está na pasta 'dados_brutos'.")
