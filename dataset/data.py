import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

data = 'State of Data 2021 - Dataset - Pgina1.csv'
df = pd.read_csv(data)



novo_nome_colunas = [
    'id', 'Idade', 'Faixa idade', 'Genero', 'Estado', 'UF',
    'Regiao onde mora', 'Regiao de origem', 'Mudou de Estado?', 'Nivel de Ensino',
    'Área de Formação', 'Qual sua situação atual de trabalho?', 'Setor',
    'Numero de Funcionarios', 'Gestor?', 'Cargo como Gestor', 'Cargo Atual',
    'Nivel', 'Faixa salarial', 'Quanto tempo de experiência na área de dados você tem?',
    'Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados?',
    'Você está satisfeito na sua empresa atual?', 'Qual o principal motivo da sua insatisfação com a empresa atual?',
    'Falta de oportunidade de crescimento no emprego atual', 'Salário atual não corresponde ao mercado',
    'Não tenho uma boa relação com meu líder/gestor', 'Gostaria de trabalhar em em outra área de atuação',
    'Gostaria de receber mais benefícios', 'O clima de trabalho/ambiente não é bom',
    'Falta de maturidade analítica na empresa', 'Você participou de entrevistas de emprego nos últimos 6 meses?',
    'Você pretende mudar de emprego nos próximos 6 meses?', 'Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?',
    'Remuneração/Salário', 'Benefícios', 'Propósito do trabalho e da empresa', 'Flexibilidade de trabalho remoto',
    'Ambiente e clima de trabalho', 'Oportunidade de aprendizado e trabalhar com referências na área',
    'Plano de carreira e oportunidades de crescimento profissional', 'Maturidade da empresa em termos de tecnologia e dados',
    'Qualidade dos gestores e líderes', 'Reputação que a empresa tem no mercado', 'Atualmente qual a sua forma de trabalho?',
    'Qual a forma de trabalho ideal para você?', 'Caso sua empresa decida pelo modelo 100% presencial qual será sua atitude?',
    'Qual o número aproximado de pessoas que atuam com dados na sua empresa hoje?',
    'Quais desses papéis/cargos fazem parte do time (ou chapter) de dados da sua empresa?',
    'Analytics Engineer', 'Engenharia de Dados/Data Engineer', 'Analista de Dados/Data Analyst', 'Cientista de Dados/Data Scientist',
    'Database Administrator/DBA', 'Analista de Business Intelligence/BI', 'Arquiteto de Dados/Data Architect', 'Data Product Manager/DPM',
    'Business Analyst', 'Quais dessas responsabilidades fazem parte da sua rotina atual de trabalho como gestor?',
    'Pensar na visão de longo prazo de dados da empresa e fortalecimento da cultura analítica da companhia.',
    'Organização de treinamentos e iniciativas com o objetivo de aumentar a maturidade analítica das áreas de negócios.',
    'Atração, seleção e contratação de talentos para o time de dados.', 'Decisão sobre contratação de ferramentas e tecnologias relacionadas a dados.',
    'Sou gestor da equipe responsável pela engenharia de dados e por manter o Data Lake da empresa como fonte única dos dados, garantindo a qualidade e confiabilidade da informação.',
    'Sou gestor da equipe responsável pela entrega de dados, estudos, relatórios e dashboards para as áreas de negócio da empresa.',
    'Sou gestor da equipe responsável por iniciativas e projetos envolvendo Inteligência Artificial e Machine Learning.',
    'Apesar de ser gestor ainda atuo na parte técnica, construindo soluções/análises/modelos etc.',
    'Gestão de projetos de dados, cuidando das etapas, equipes envolvidas, atingimento dos objetivos etc.',
    'Gestão de produtos de dados, cuidando da visão dos produtos, backlog, feedback de usuários etc.',
    'Gestão de pessoas, apoio no desenvolvimento das pessoas, evolução de carreira', 'Quais são os 3 maiores desafios que você tem como gestor no atual momento?',
    'a Contratar novos talentos.', 'b Reter talentos.', 'c Convencer a empresa a aumentar os investimentos na área de dados.',
    'd Gestão de equipes no ambiente remoto.', 'e Gestão de projetos envolvendo áreas multidisciplinares da empresa.',
    'f Organizar as informações e garantir a qualidade e confiabilidade.', 'g Conseguir processar e armazenar um alto volume de dados.',
    'h Conseguir gerar valor para as áreas de negócios através de estudos e experimentos.', 'i Desenvolver e manter modelos Machine Learning em produção.',
    'j Gerenciar a expectativa das áreas de negócio em relação as entregas das equipes de dados.', 'k Garantir a manutenção dos projetos e modelos em produção, em meio ao crescimento da empresa.',
    'Conseguir levar inovação para a empresa através dos dados.', 'Garantir retorno do investimento (ROI) em projetos de dados.', 'Dividir o tempo entre entregas técnicas e gestão.',
    'Atuacao', 'Mesmo que esse não seja seu cargo formal, você considera que sua atuação no dia a dia, reflete alguma das opções listadas abaixo?', 'Atuação',
    'Quais das fontes de dados listadas você já analisou ou processou no trabalho?', 'Dados relacionais (estruturados em bancos SQL)',
    'Dados armazenados em bancos NoSQL', 'Imagens', 'Textos/Documentos', 'Vídeos', 'Áudios', 'Planilhas', 'Dados georeferenciados',
    'Entre as fontes de dados listadas, quais você utiliza na maior parte do tempo?', 'Dados relacionais (estruturados em bancos SQL)',
    'Dados armazenados em bancos NoSQL', 'Imagens', 'Textos/Documentos', 'Vídeos', 'Áudios', 'Planilhas', 'Dados georeferenciados',
    'Quais das linguagens listadas abaixo você utiliza no trabalho?', 'SQL', 'R ', 'Python', 'C/C++/C#', '.NET', 'Java', 'Julia', 'SAS/Stata',
    'Visual Basic/VBA', 'Scala', 'Matlab', 'PHP', 'Javascript', 'Não utilizo nenhuma linguagem',
    'Entre as linguagens listadas abaixo, qual é a que você mais utiliza no trabalho?', 'SQL', 'R ', 'Python', 'C/C++/C#', '.NET', 'Java', 'Julia', 'SAS/Stata',
    'Visual Basic/VBA', 'Scala', 'Matlab', 'PHP', 'Javascript', 'Não utilizo nenhuma linguagem',
    'Quais dos bancos de dados/fontes de dados listados abaixo você utiliza no trabalho?', 'MySQL', 'Oracle', 'SQL SERVER', 'SAP', 'Amazon Aurora ou RDS',
    'Amazon DynamoDB', 'CoachDB', 'Cassandra', 'MongoDB', 'MariaDB', 'Datomic', 'S3', 'PostgreSQL', 'ElasticSearch', 'DB2', 'Microsoft Access', 'SQLite',
    'Sybase', 'Firebase', 'Vertica', 'Redis', 'Neo4J', 'Google BigQuery', 'Google Firestore', 'Amazon Redshift', 'Amazon Athena', 'Snowflake', 'Databricks',
    'HBase', 'Presto', 'Splunk', 'SAP HANA', 'Hive', 'Firebird', 'Quais das opções de Cloud listadas abaixo você utiliza no trabalho?',
    'Amazon Web Services (AWS)', 'Google Cloud (GCP)', 'Azure (Microsoft)', 'Oracle Cloud', 'IBM', 'Servidores On Premise/Não utilizamos Cloud', 'Cloud Própria',
    'Quais as Ferramentas de Business Intelligence você utiliza no trabalho?', 'Microsoft PowerBI', 'Qlik View/Qlik Sense', 'Tableau', 'Metabase', 'Superset',
    'Redash', 'MicroStrategy', 'IBM Analytics/Cognos', 'SAP Business Objects', 'Oracle Business Intelligence', 'Amazon QuickSight', 'Salesforce/Einstein Analytics',
    'Mode', 'Alteryx', 'Birst', 'Looker', 'Google Data Studio', 'SAS Visual Analytics', 'Grafana', 'TIBCO Spotfire', 'Pentaho',
    'Fazemos todas as análises utilizando apenas Excel ou planilhas do google', 'Não utilizo nenhuma ferramenta de BI no trabalho',
    'Qual oportunidade você está buscando?', 'Há quanto tempo você busca uma oportunidade na área de dados?', 'Como tem sido a busca por um emprego na área de dados?',  'Quais das opções abaixo fazem parte da sua rotina no trabalho atual como engenheiro de dados?',
    'Desenvolvo pipelines de dados utilizando linguagens de programação como Python, Scala, Java etc.',
    'Realizo construções de ETLs em ferramentas como Pentaho, Talend, Dataflow etc.',
    'Crio consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.',
    'Atuo na integração de diferentes fontes de dados através de plataformas proprietárias como Stitch Data, Fivetran etc.',
    'Modelo soluções de arquitetura de dados, criando componentes de ingestão de dados, transformação e recuperação da informação.',
    'Desenvolvo/cuido da manutenção de repositórios de dados baseados em streaming de eventos como Data Lakes e Data Lakehouses.',
    'Atuo na modelagem dos dados, com o objetivo de criar conjuntos de dados como Data Warehouses, Data Marts etc.',
    'Cuido da qualidade dos dados, metadados e dicionário de dados.',
    'Nenhuma das opções listadas refletem meu dia a dia.',
    'Quais as ferramentas/tecnologias de ETL que você utiliza no trabalho como Data Engineer?',
    'Scripts Python',
    'SQL & Stored Procedures',
    'Apache Airflow',
    'Luigi',
    'AWS Glue',
    'Talend',
    'Stitch',
    'Fivetran',
    'Google Dataflow',
    'Oracle Data Integrator',
    'IBM DataStage',
    'SAP BW ETL',
    'SQL Server Integration Services (SSIS)',
    'SAS Data Integration',
    'Qlik Sense',
    'Knime',
    'Não utilizo ferramentas de ETL',
    'Sua organização possui um Data Lake?',
    'Qual tecnologia utilizada como plataforma do Data Lake?',
    'Sua organização possui um Data Warehouse?',
    'Qual tecnologia utilizada como plataforma do Data Warehouse?',
    'Quais as ferramentas de gestão de Qualidade de dados, Metadados e catálogo de dados você utiliza no trabalho?',
    'great_expectations',
    'dbt',
    'AWS Deequ',
    'Apache Griffin',
    'Datafold',
    'Amundsen',
    'Monte Carlo',
    'SODA',
    'Big Eye',
    'Data Band',
    'Anomalo',
    'Metaplane',
    'Acceldata',
    'Em qual das opções abaixo você gasta a maior parte do seu tempo?',
    'Desenvolvendo pipelines de dados utilizando linguagens de programação como Python, Scala, Java etc.',
    'Realizando construções de ETLs em ferramentas como Pentaho, Talend, Dataflow etc.',
    'Criando consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.',
    'Atuando na integração de diferentes fontes de dados através de plataformas proprietárias como Stitch Data, Fivetran etc.',
    'Modelando soluções de arquitetura de dados, criando componentes de ingestão de dados, transformação e recuperação da informação.',
    'Desenvolvendo/cuidando da manutenção de repositórios de dados baseados em streaming de eventos como Data Lakes e Data Lakehouses.',
    'Atuando na modelagem dos dados, com o objetivo de criar conjuntos de dados como Data Warehouses, Data Marts etc.',
    'Cuidando da qualidade dos dados, metadados e dicionário de dados.',
    'Quais das opções abaixo fazem parte da sua rotina no trabalho atual com análise de dados?',
    'Processo e analiso dados utilizando linguagens de programação como Python, R etc.',
    'Realizo construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik etc.',
    'Utilizo API\'s para extrair dados e complementar minhas análises.',
    'Realizo experimentos e estudos utilizando metodologias estatísticas como teste de hipótese, modelos de regressão etc.',
    'Desenvolvo/cuido da manutenção de ETL\'s utilizando tecnologias como Talend, Pentaho, Airflow, Dataflow etc.',
    'Atuo na modelagem dos dados, com o objetivo de criar conjuntos de dados, Data Warehouses, Data Marts etc.',
    'Desenvolvo/cuido da manutenção de planilhas para atender as áreas de negócio.',
    'Utilizo ferramentas avançadas de estatística como SAS',
    'Quais as ferramentas/tecnologias de ETL que você utiliza no trabalho como Data Analyst?',
    'Scripts Python',
    'SQL & Stored Procedures',
    'Apache Airflow',
    'Luigi',
    'AWS Glue',
    'Talend',
    'Stitch',
    'Fivetran',
    'Google Dataflow',
    'Oracle Data Integrator',
    'IBM DataStage',
    'SAP BW ETL',
    'SQL Server Integration Services (SSIS)',
    'SAS Data Integration',
    'Qlik Sense',
    'Knime',
    'Não utilizo ferramentas de ETL',
    'Sua empresa utiliza alguma das ferramentas listadas para dar mais autonomia em análise de dados para as áreas de negócio?',
    'Ferramentas de AutoML como H2O.ai, Data Robot, BigML etc.',
    '"Point and Click" Analytics como Alteryx, Knime, Rapidminer etc.',
    'Product metricts & Insights como Mixpanel, Amplitude, Adobe Analytics.',
    'Ferramentas de análise dentro de ferramentas de CRM como Salesforce Einstein Anaytics ou Zendesk dashboards.',
    'Minha empresa não utiliza essas ferramentas.',
    'Não sei informar.',
    'Em qual das opções abaixo você gasta a maior parte do seu tempo de trabalho?',
    'Processando e analisando dados utilizando linguagens de programação como Python, R etc.',
    'Realizando construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik etc.',
    'Utilizando API\'s para extrair dados e complementar minhas análises.',
    'Realizando experimentos e estudos utilizando metodologias estatísticas como teste de hipótese, modelos de regressão etc.',
    'Desenvolvendo/cuidando da manutenção de ETL\'s utilizando tecnologias como Talend, Pentaho, Airflow, Dataflow etc.',
    'Atuando na modelagem dos dados, com o objetivo de criar conjuntos de dados, Data Warehouses, Data Marts etc.',
    'Desenvolvendo/cuidando da manutenção de planilhas do Excel ou Google Sheets para atender as áreas de negócio.',
    'Utilizando ferramentas avançadas de estatística como SAS, SPSS, Stata etc, para realizar análises.',
    'Quais das opções abaixo fazem parte da sua rotina no trabalho atual com ciência de dados?',
    'Estudos Ad-hoc com o objetivo de confirmar hipóteses, realizar modelos preditivos, forecasts, análise de cluster para resolver problemas pontuais e responder perguntas das áreas de negócio.',
    'Sou responsável pela coleta e limpeza dos dados que uso para análise e modelagem.',
    'Sou responsável por entrar em contato com os times de negócio para definição do problema, identificar a solução e apresentação de resultados.',
    'Desenvolvo modelos de Machine Learning com o objetivo de colocar em produção em sistemas (produtos de dados).',
    'Sou responsável por colocar modelos em produção, criar os pipelines de dados, APIs de consumo e monitoramento.',
    'Cuido da manutenção de modelos de Machine Learning já em produção, atuando no monitoramento, ajustes e refatoração quando necessário.',
    'Realizo construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik, etc',
    'Utilizo ferramentas avançadas de estatística como SAS, SPSS, Stata etc, para realizar análises estatísticas e ajustar modelos.Crio e dou manutenção em ETLs, DAGs e automações de pipelines de dados.',
    'Sou responsável por criar e manter a infra que meus modelos e soluções rodam (clusters, servidores, API, containers, etc.)',
    'Quais as técnicas e métodos listados abaixo você costuma utilizar no trabalho?',
    'Utilizo modelos de regressão (linear, logística, GLM)',
    'Utilizo redes neurais ou modelos baseados em árvore para criar modelos de classificação',
    'Desenvolvo sistemas de recomendação (RecSys)',
    'Utilizo métodos estatísticos Bayesianos para analisar dados',
    'Utilizo técnicas de NLP (Natural Language Processing) para análisar dados não-estruturados',
    'Utilizo métodos estatísticos clássicos (Testes de hipótese, análise multivariada, sobrevivência, dados longitudinais, inferência estatistica) para analisar dados',
    'Utilizo cadeias de Markov ou HMM\'s para realizar análises de dados',
    'Utilizo modelos de Séries Temporais (Time Series)',
    'Utilizo modelos de Reinforcement Learning (aprendizado por reforço)',
    'Utilizo modelos de Machine Learning para detecção de fraude',
    'Utilizo métodos de Visão Computacional',
    'Utilizo modelos de Detecção de Churn',
    'Quais dessas tecnologias fazem parte do seu dia a dia como cientista de dados?',
    'Ferramentas de BI (PowerBI, Looker, Tableau, Qlik etc)',
    'Planilhas (Excel, Google Sheets etc)',
    'Ambientes de desenvolvimento local (R-studio, JupyterLab, Anaconda)',
    'Ambientes de desenvolvimento na nuvem (Google Colab, AWS Sagemaker, Kaggle Notebooks etc)',
    'Ferramentas de AutoML (Datarobot, H2O, Auto-Keras etc)',
    'Ferramentas de ETL (Apache Airflow, NiFi, Stitch, Fivetran, Pentaho etc)',
    'Plataformas de Machine Learning (TensorFlow, Azure Machine Learning, Kubeflow etc)',
    'Feature Store (Feast, Hopsworks, AWS Feature Store, Databricks Feature Store etc)',
    'Sistemas de controle de versão (Github, DVC, Neptune, Gitlab etc)',
    'Plataformas de Data Apps (Streamlit, Shiny, Plotly Dash etc)',
    'Ferramentas de estatística avançada como SPSS, SAS, etc.',
    'Não utilizo nenhuma dessas ferramentas no meu dia a dia.',
    'Em qual das opções abaixo você gasta a maior parte do seu tempo no trabalho?',
    'Coletando e limpando os dados que uso para análise e modelagem.',
    'Entrando em contato com os times de negócio para definição do problema, identificar a solução e apresentação de resultados.',
    'Desenvolvendo modelos de Machine Learning com o objetivo de colocar em produção em sistemas (produtos de dados).',
    'Colocando modelos em produção, criando os pipelines de dados, APIs de consumo e monitoramento.',
    'Cuidando da manutenção de modelos de Machine Learning já em produção, atuando no monitoramento, ajustes e refatoração quando necessário.',
    'Realizando construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik, etc.',
    'Criando e dando manutenção em ETLs, DAGs e automações de pipelines de dados.',
    'Criando e gerenciando soluções de Feature Store e cultura de MLOps.',
    'Criando e mantendo a infra que meus modelos e soluções rodam (clusters, servidores, API, containers, etc.)',
    'Quais das iniciativas do Data Hackers que você já acessou/acompanhou?',
    'Blog/Medium do Data Hackers',
    'Podcast do Data Hackers',
    'Newsletter Semanal',
    'Canal do Slack',
    'Canal do Youtube do Data Hackers',
    'Ainda não conhecia o Data Hackers']

# Renomeie as colunas do DataFrame
df.columns = novo_nome_colunas
data2 = 'df_novo'
df.to_csv(data2)

#Substituindo NA
df = df.fillna("Não informado")
## Padronizar os valores da coluna "Cargo Atual" para letras minúsculas
df['Cargo Atual'] = df['Cargo Atual'].str.lower()
################################################################################################################
'ANALISES'

# Exibindo a distribuição dos níveis de ensino de todo o dataset
nivel_ensino_counts = df['Nivel de Ensino'].value_counts()
plt.figure(figsize=(10, 6))
nivel_ensino_counts.plot(kind='bar', color='red')
plt.title('Distribuição dos Níveis de Ensino')
plt.xlabel('Nível de Ensino')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Exibindo a distribuição dos níveis de ensino dos GESTORES
gestores_df = df[df['Gestor?'] == 1]
nivel_ensino_counts_gestores = gestores_df['Nivel de Ensino'].value_counts()
plt.figure(figsize=(10, 6))
nivel_ensino_counts_gestores.plot(kind='bar', color='blue')
plt.title('Distribuição dos Níveis de Ensino para Gestores')
plt.xlabel('Nível de Ensino')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_salario_cargo = df[['Cargo Atual', 'Faixa salarial']]
df_salario_cargo = df_salario_cargo[df_salario_cargo['Cargo Atual'] != 'não informado']

# Limpar a coluna 'Faixa salarial' para manter apenas valores numéricos
df_salario_cargo['Faixa salarial'] = df_salario_cargo['Faixa salarial'].str.extract(r'(\d+\.\d+)').astype(float)

salario_por_cargo = df_salario_cargo.groupby('Cargo Atual')['Faixa salarial'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(8, 8))
salario_por_cargo.plot(kind='bar', color='red')
plt.title('Top 5 Cargos com Maiores Salários Médios')
plt.xlabel('Cargo Atual', fontsize = 12)
plt.ylabel('Média de Salário')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Imprimir a quantidade de pessoas por cargo
quantidade_pessoas_por_cargo = df_salario_cargo['Cargo Atual'].value_counts()
print('Quantidade de Pessoas por Cargo:')
print(quantidade_pessoas_por_cargo)

#############################################################################################################################

# Verifique se a coluna 'Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?' existe
if 'Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?' in df.columns:
    # Extraia as respostas para a pergunta sobre critérios de decisão
    respostas_critérios = df['Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?'].dropna()
    # Divida as respostas em palavras-chave (você pode ajustar isso conforme necessário)
    palavras_chave = ['salário', 'oportunidade', 'clima', 'benefícios', 'tecnologia', 'crescimento', 'liderança']
    # Inicialize um dicionário para contar a frequência de cada palavra-chave
    contagem_critérios = {palavra: 0 for palavra in palavras_chave}
    # Conte a frequência de cada palavra-chave nas respostas
    for resposta in respostas_critérios:
        for palavra in palavras_chave:
            if palavra in resposta.lower():
                contagem_critérios[palavra] += 1
    for palavra, contagem in contagem_critérios.items():
        print(f'{palavra.capitalize()}: {contagem} vezes')
    # Crie o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(contagem_critérios.keys(), contagem_critérios.values())
    plt.xlabel('Critérios de Decisão')
    plt.ylabel('Contagem')
    plt.title('Contagem dos Critérios que Influenciam a Decisão de Mudar de Emprego')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Exiba o gráfico
    plt.show()
else:
    print('A coluna especificada não existe no conjunto de dados.')



# Verifique se a coluna 'Idade' existe
if 'Idade' in df.columns:
    # Remova possíveis valores não numéricos da coluna 'Idade'
    df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')
    # Calcule as estatísticas descritivas da idade
    idade_media = df['Idade'].mean()
    idade_mediana = df['Idade'].median()
    idade_minima = df['Idade'].min()
    idade_maxima = df['Idade'].max()
    idade_desvio_padrao = df['Idade'].std()
    # Exiba as estatísticas descritivas
    print(f"\nMédia de Idade: {idade_media:.2f} anos")
    print(f"Mediana de Idade: {idade_mediana} anos")
    print(f"Idade Mínima: {idade_minima} anos")
    print(f"Idade Máxima: {idade_maxima} anos")
    print(f"Desvio Padrão de Idade: {idade_desvio_padrao:.2f} anos")
else:
    print('A coluna "Idade" não existe no conjunto de dados ou contém valores não numéricos.')


#############################################################################################################################

# Gráfico de barras, distribuição de setores
df = df[df['Setor'] != 'Não informado']
plt.figure(figsize=(12, 6))
sns.countplot(y='Setor', data=df, palette='viridis')
plt.title('Distribuição de Setores')
plt.xlabel('Contagem')
plt.ylabel('Setor')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos e alinha à direita para melhor legibilidade
plt.tight_layout()
plt.show()

# Função para extrair a média de salário
def extrair_media(faixa_salarial):
    if isinstance(faixa_salarial, str):
        valores = re.findall(r'R\$\s([\d,.]+)', faixa_salarial)
        valores = [float(valor.replace(',', '').replace('.', '')) for valor in valores]
        if valores:
            return sum(valores) / len(valores)
        else:
            return 0
    else:
        return 0

# Aplicar a função para extrair a média de salário para cada linha
df['Media de Salario'] = df['Faixa salarial'].apply(extrair_media)
df = df[df['Genero'] != 'Outro']
# Agrupe os dados por gênero e calcule a média de salário para cada grupo
media_salario_por_genero = df.groupby('Genero')['Media de Salario'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Genero', y='Media de Salario', data=media_salario_por_genero, palette='viridis')
plt.xlabel('Gênero')
plt.ylabel('Média de Salário')
plt.title('Média de Salário por Sexo')
plt.xticks(rotation=0)  # Mantém os rótulos do eixo x na posição padrão
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#COMPARAÇÃO DE SALARIO COM O MESMO CARGO
cargos_comuns = set(df[df['Genero'] == 'Masculino']['Cargo Atual']).intersection(set(df[df['Genero'] == 'Feminino']['Cargo Atual']))
df_cargos_comuns = df[df['Cargo Atual'].isin(cargos_comuns)]
plt.figure(figsize=(12, 8))
sns.barplot(x='Cargo Atual', y='Media de Salario', hue='Genero', data=df_cargos_comuns, palette='Set2')
plt.title('Comparação Salarial entre Homens e Mulheres nos Mesmos Cargos')
plt.xlabel('Cargo')
plt.ylabel('Média de Salário')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



