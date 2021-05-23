# Analise_Custos_Medicos
Análise de dados e implantação de um modelo de machine learning para prever custos de gastos em planos médicos com base nas informações de planos contratados anteriormente.

+ **Previsao_Custos_Medicos.ipynb** - Arquivo jupyter com os tratamentos e anotações que juguei necessárias utilizando programação em python
+ **insurance.csv** - Arquivo base com os dados das pessoas que tem custos médicos registrados, possibilitando assim a análise exploratória dos dados históricos. Essa base de dados foi obtida no site kaggle (link: https://www.kaggle.com/mirichoi0218/insurance)
+ **data_deploy.csv** - Arquivo gerado após os tratamentos e aplicação do modelo de machine learning, nele já constam os dados que o modelo de previsão necessita para gerar os resultados que neste caso serão utilizados na construção de um Web Data App com o intuito de gerar previsões personalizadas. 
+ **app_custos.py** - Arquivo contendo algoritmo python para inserção do modelo de machine learning juntamente com uma aplicação web que possibilita ao usuário final preencher os dados que determina o preço do custo do plano médico do cliente. 
