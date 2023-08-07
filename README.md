# Engenharia_de_Dados_Cine_Prime

O Projeto de Engenharia de Dados, em sua maioria - e sendo generalista, abrange três etapas, sendo elas: Extração, Limpeza e o Carregamento dos Dados. Essas etapas contribuem à qualidade dos dados. Dessa forma, para manutenção da cultura data driven - apoiando nas tomadas de decisões, a partir dos conhecimentos adquiridos nessa temática, extrairei, tratarei e carregarei os dados informados na fonte 'https://www.imdb.com/chart/top?ref_=nv_mv_250'.

A ideia central é, posterior à coleta das informações, tratamentoe limpeza dos dados, gerar um arquivo csv com os devidos ajustes. Um detalhe em questão é, além de armazenar os valores já disponibilizados, marcar um 'S', em uma coluna de nome 'Escolhido', para filmes com média >= 9,0, caso contrário, marcar um 'N'.

Obs.: Caso surja alguma eventualidade na execução do código (que inicia-se no código executar.py), atente-se ao arquivo logger. Além disso, fiz uso de variáveis de ambiente para acessar o banco, então, para garantir a funcionalidade do código, será necessário informá-las, segue a estrutura que utilizei para armazenar os dados:

Nome do arquivo: .env

DATABASE="XXXXXXXXX"
HOST="XXXXXXXXXXXXX"
USER="XXXXXXXXXXXXX"
PASSWORD="XXXXXXXXX"
PORT="XXXXXXXXXXXXX"