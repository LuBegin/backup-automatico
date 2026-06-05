import os
import shutil
import datetime
import schedule
import time

origem_dir = "C:/Users/Ana & Malu/Desktop/indie christian artists"
destino_dir = "C:/Users/Ana & Malu/Desktop/Backup" 

def copiar_pasta_para_diretório(origem, destino):
    hoje = datetime.date.today()
    dest_dir = os.path.join(destino, str(hoje))


    try: 
        shutil.copytree(origem, dest_dir)
        print(f"Pasta copiada para: {dest_dir}")
    except FileExistsError:
        print(f"Pasta já existe em: {dest_dir}")


copiar_pasta_para_diretório(origem_dir, destino_dir)
if "Pasta copiada para: {dest_dir}":
    print("Backup realizado com sucesso!")
else:
    print("Aguardando...")

schedule.every().day.at("21:31").do(copiar_pasta_para_diretório, origem_dir, destino_dir)


while True:
    schedule.run_pending()
    time.sleep(60)