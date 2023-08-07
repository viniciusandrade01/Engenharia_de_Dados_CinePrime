from datetime import datetime
import logging
import os
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests as rq

class Utils:
    def __init__(self):
        self.reg = r"(\d+)\. (.+?)(\d{4})(\d+h \d+m)(?:Livre)?(\d+\.\d+)Rate"
        self.year = datetime.now().strftime('%Y')
        
    def regex_insercao(self, texto: BeautifulSoup):
        matches = re.findall(self.reg, texto.get_text(), re.MULTILINE)
        
        data_list = []
        for match in matches:
            data_dict = {
                'Index': int(match[0]),
                'Titulo': match[1],
                'Ano': int(match[2]),
                'Duração': match[3],
                'Classificação': str(match[4][:2]).replace(".",""),
                'Avaliação': float(match[4][2:]),
                'Escolhido': 'S' if float(match[4][2:]) >= 9 else 'N'
            }
            data_list.append(data_dict)

        # Criar um DataFrame a partir da lista de dicionários
        df = pd.DataFrame.from_records(data_list)
        return df
    
    def criando_diretorio(self):
        # Solicitação do nome do diretório e verificação se há valor no diretório
        diretorio = input("Digite o nome do diretório para armazenar o csv gerado (exemplo: Coleta): ")
        diretorio = diretorio or "Coleta"
        logging.info("Diretório destino informado com sucesso!")
        logging.info("Obs.: Caso não tenha sido preenchido, o nome padrão ('Coleta') será adotado")
        
        # Verificar se o diretório existe, e se não existir, criá-lo
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        return diretorio
    
    def nomeando_arquivo(self):
        # Solicitação do nome do arquivo e verificação se há valor no arquivo
        arquivo = input(f"Digite o nome para o arquivo csv gerado (exemplo: Cine_Rank_{self.year}): ")
        arquivo = f"Cinema_Ranking_{self.year}.csv" if len(arquivo) == 0 else f"{arquivo}.csv"
        logging.info("Nome do arquivo gerado informado com sucesso!")
        logging.info("Obs.: Caso não tenha sido preenchido, o nome padrão ('Cine_Rank_{self.year}') será     adotado")
        
        return arquivo
    
    def requisicao(self, fonte: str):
        try:
            # Fazer a requisição HTTP
            req = rq.get(fonte, 
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
            
        return info_filmes