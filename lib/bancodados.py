from datetime import datetime
import psycopg2
import os
import logging
import pandas as pd
from sqlalchemy import create_engine

class Banco:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = os.getenv("HOST"),
            database = os.getenv("DATABASE"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            port = os.getenv("PORT")
        )
        logging.info("BD conectado com sucesso!") if self.conn.status == 1 else logging.error("Falha ao conectar-se ao BD.")

    def usando_banco(self, df: pd.DataFrame):
        # Criação de um cursor para executar comandos SQL
        cur = self.conn.cursor()
        
        # Pegando o nome do primeiro arquivo sql encontrado no diretório e 'lendo' o arquivo
        with open([arquivo for arquivo in os.listdir(os.getcwd()) if arquivo.endswith(".sql")][0], 'r') as sql_file:
            sql_script = sql_file.read()

        # Executando a instrução SQL defina para criação da tabela
        cur.execute(sql_script.split("\n\n")[0])
        
        # Inserir o DataFrame no banco de dados usando a conexão existente (self.conn)
        db_url = f"postgresql+psycopg2://{self.conn.dsn.split(' ')[0].split('=')[1]}:123456@{self.conn.dsn.split(' ')[-2].split('=')[1]}:{self.conn.dsn.split(' ')[-1].split('=')[1]}/data_cine"
        engine = create_engine(db_url)
        df.to_sql(sql_script.split(" (\n")[0].split(" ")[-1], engine, if_exists='replace', index=False)

        # Confirma a transação
        self.conn.commit()
        logging.info("Dados carregados com sucesso!")
        
        # Execute uma consulta para selecionar todos os valores da tabela
        cur.execute(sql_script.split("\n\n")[1])

        # Recupere os resultados da consulta
        results = cur.fetchall()

        # Desabilite para visualizar os resultados inseridos no Banco de Dados
        for row in results:
            print(row)

        # Fechando o cursor e a conexão
        cur.close()
        self.conn.close()