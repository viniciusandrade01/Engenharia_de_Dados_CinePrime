import os
import logging
from datetime import datetime
from lib.utils import Utils
from lib.bancodados import Banco

# Instâncias criada, localizada dentro da pasta lib, dos códigos: utils e banco de dados.
utl = Utils()
bc = Banco()

# Configura o logger
logging.basicConfig(filename=os.path.dirname(os.path.abspath(__file__)) + f"\\Log_{datetime.now().strftime('%Y_%m_%d')}.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d__%H%M%S")
    
# Solicitação do nome do diretório, verificação se há valor no diretório e criação dele
diretorio = utl.criando_diretorio()

# Solicitação do nome do arquivo e verificação se há valor no arquivo
arquivo = utl.nomeando_arquivo()

info_filmes = utl.requisicao("https://www.imdb.com/chart/top?ref_=nv_mv_250")

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
bc.usando_banco(df)
logging.info("Banco usado!")
logging.info("Encerrando sistema!")
logging.info("-------------------------------")