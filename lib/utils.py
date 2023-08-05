import pandas as pd
from bs4 import BeautifulSoup
import re

class Utils:
    #def __init__(self, nome, idade, profissao):
    #    self.nome = nome
    #    self.idade = idade
    #    self.profissao = profissao
    #
    #def apresentar(self):
    #    print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")
    #
    #def envelhecer(self, anos):
    #    self.idade += anos
    #    print(f"Envelheci {anos} anos. Agora tenho {self.idade} anos.")
    def __init__(self):
        self.reg = r"(\d+)\. (.+?)(\d{4})(\d+h \d+m)(?:Livre)?(\d+\.\d+)Rate"
        
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
        

# Criando uma instância da classe
#pessoa = Utils("João", 30, "Engenheiro")

# Chamando métodos da classe
#pessoa.apresentar()
#pessoa.envelhecer(5)
#pessoa.apresentar()
