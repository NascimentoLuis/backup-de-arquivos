import os
import shutil
import time
from datetime import datetime


# Solicita ao usuário os diretórios de origem e destino
origem = input("Digite o caminho da pasta que deseja fazer backup: ").strip()
destino = input("Dgite o caminho da pasta onde deseja salvar o backup: ").strip()



# Verifica se o diretório de irgem existe
if not os.path.exists(origem):
    print("Erro: O diretório de origem não existe. Verifique o caminho e tente novamente.")
    exit()


# Cria um nome para a pasta de backup com data e hora
data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
pasta_backup = os.path.join(destino, f"backup_{data_atual}") 

# Cria a pasta de backup
os.makedirs(pasta_backup, exist_ok=True)

# Copia os arquivos

try:
    for item in os.listdir(origem):
        caminho_origem = os.path.join(origem, item)
        caminho_destino = os.path.join(pasta_backup, item)


        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
        elif os.path.isdir(caminho_origem):
            shutil.copytree(caminho_origem, caminho_destino)

    print(f"\n Backup concluído com sucesso! Arquivos salvos em: {pasta_backup}")


except Exception as e:
    print(f"\n Erro ao fazer backup: {e}")                
    
