# Engenharia_de_Dados_Cine_Prime
O Projeto de Engenharia de Dados, em sua maioria - e sendo generalista, abrange três etapas, sendo elas: Extração, Tratamento e o Carregamento (ETL) dos Dados. Essas etapas contribuem à qualidade dos dados. Dessa forma, para manutenção da cultura data driven - apoiando nas tomadas de decisões, a partir dos conhecimentos adquiridos nessa temática, extrai, tratei e carreguei os dados informados na fonte 'https://www.imdb.com/chart/top?ref_=nv_mv_250'.

A ideia central foi, posterior à coleta das informações, tratar os dados e carregará-los no Banco de Dados PostgreSQL, conforme fiz. Um detalhe em questão é, além do armazenamento dos valores já disponibilizados na fonte, atribuí um 'S', em uma coluna de nome 'Escolhido', para filmes com média >= 9,0, caso contrário, 'N'. Essa coluna, embora 'simples', é considerada de grande valia, pois será utilizada para raning dos filmes mais bem avaliados no cenário contemporâneo, auxiliando em ações de marketing.

Obs.: Caso surja alguma eventualidade na execução do código (que inicia-se no código executar.py), atente-se ao arquivo log. Além disso, fiz uso de variáveis de ambiente para acessar o banco, então, para garantir a plena funcionalidade do código, será necessário informá-las, segue a estrutura que utilizei para armazenar os dados:

Nome do arquivo: .env

DATABASE="XXXXXXXXX"
HOST="XXXXXXXXXXXXX"
USER="XXXXXXXXXXXXX"
PASSWORD="XXXXXXXXX"
PORT="XXXXXXXXXXXXX"