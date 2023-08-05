import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import os
import psycopg2
import logging
from datetime import datetime
from lib.utils import Utils
from lib.bancodados import Banco

# Instância da classe Geral criada, localizada dentro da pasta lib, do código utils
utl = Utils()
bc = Banco()

# Configura o logger
logging.basicConfig(filename=f"Log_{datetime.now().strftime('%Y_%m_%d')}.log", 
                    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d__%H%M%S")
    
# Solicitação do nome do diretório e verificação se há valor no diretório
year = datetime.now().strftime('%Y')
diretorio = input("Digite o nome do diretório para armazenar o csv gerado (exemplo: Coleta): ")
diretorio = diretorio or "Coleta"
logging.info("Diretório destino informado com sucesso!")
logging.info("Obs.: Caso não tenha sido preenchido, o nome padrão ('Coleta') será adotado")

# Solicitação do nome do arquivo e verificação se há valor no arquivo
arquivo = input(f"Digite o nome para o arquivo csv gerado (exemplo: Cine_Rank_{year}): ")
arquivo = f"Cinema_Ranking_{year}.csv" if len(arquivo) == 0 else f"{arquivo}.csv"
logging.info("Nome do arquivo gerado informado com sucesso!")
logging.info("Obs.: Caso não tenha sido preenchido, o nome padrão ('Cine_Rank_{year}') será adotado")

# Verificar se o diretório existe, e se não existir, criá-lo
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

try:
    # Fazer a requisição HTTP
    req = rq.get("https://www.imdb.com/chart/top?ref_=nv_mv_250", 
                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

    if req.status_code == 200:
        logging.info('Requisição bem sucedida!')
        content = req.content
    else:
        logging.error("Não foi possível acessar à requisição!")
        raise SystemExit("Programa interrompido devido à falha na requisição.")

    try:
        # Analisar o conteúdo da página usando BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Encontrar a tabela de filmes
        table = soup.find('tbody', class_='lister-list')

        # Encontrar informações sobre os filmes
        info_filmes = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base')
        logging.info("Elemento encontrado com sucesso!")

    except AttributeError:
        # Tratar a exceção caso o elemento não seja encontrado
        logging.error("Erro ao encontrar o elemento.")

except rq.exceptions.RequestException as e:
    # Tratar exceções de requisição
    logging.error("Erro de requisição: %s", e)
except Exception as e:
    # Tratar outras exceções não previstas
    logging.error("Ocorreu um erro inesperado: %s", e)

#df = utl.regex(info_filmes, total_filmes)
df = utl.regex_insercao(info_filmes)

# Remove linhas duplicadas + inplace
df.drop_duplicates(inplace=True)

# Reseta os indexes da tabela
df.reset_index(drop=True, inplace=True)

# Gera um arquivo csv, que irei inserir no PostgreSQL
df.to_csv(os.path.join(diretorio, arquivo), sep="\t", index=False, encoding = "utf-8")
logging.info("Arquivo tratado gerado com sucesso!!")

# Acessa função para utilizar o Banco de Dados
#bc.usando_banco(df)
logging.info("Banco usado!")
logging.info("-------------------------------")