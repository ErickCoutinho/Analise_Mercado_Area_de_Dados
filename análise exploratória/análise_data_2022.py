import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

#carregando data
data = 'data_hackers_pre.csv'
df = pd.read_csv(data)
df = df.fillna('Não Informado')
cores_degrade_roxo_verde = [
    "#800080",  # Roxo escuro
    "#9440DB",
    "#A97DF1",
    "#C0ABE8",
    "#D6E4DC",  # Verde claro
    "#A2D2A1",
    "#4CAF50"   # Verde
]
#ANÁLISE COMPARATIVA COM O DATASET DE 2021
# Exibindo a distribuição dos níveis de ensino de todo o dataset
nivel_ensino_counts = df['P1_l _Nivel de Ensino'].value_counts()
plt.figure(figsize=(10, 6))
nivel_ensino_counts.plot(kind='bar', color=cores_degrade_roxo_verde)
plt.title('Distribuição dos Níveis de Ensino')
plt.xlabel('Nível de Ensino')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Exibindo a distribuição dos níveis de ensino dos GESTORES
gestores_df = df[df['P2_d _Gestor?'] == 1]
nivel_ensino_counts_gestores = gestores_df['P1_l _Nivel de Ensino'].value_counts()
plt.figure(figsize=(10, 6))
nivel_ensino_counts_gestores.plot(kind='bar', color=cores_degrade_roxo_verde)
plt.title('Distribuição dos Níveis de Ensino para Gestores')
plt.xlabel('Nível de Ensino')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribuição de setores
df = df[df['P2_b _Setor'] != 'Não informado']
plt.figure(figsize=(12, 6))
sns.countplot(y='P2_b _Setor', data=df,hue='P2_b _Setor', palette='viridis')
plt.title('Distribuição de Setores')
plt.xlabel('Contagem')
plt.ylabel('Setor')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

linguagem_cols = [
    'P4_d_1 _SQL',
    'P4_d_2 _R ',
    'P4_d_3 _Python',
    'P4_d_4 _C/C++/C#',
    'P4_d_5 _.NET',
    'P4_d_6 _Java',
    'P4_d_7 _Julia',
    'P4_d_8 _SAS/Stata',
    'P4_d_9 _Visual Basic/VBA',
    'P4_d_10 _Scala',
    'P4_d_11 _Matlab',
    'P4_d_12 _PHP',
    'P4_d_13 _Javascript'
]

# Converter as colunas para tipo numérico, tratando 'Sim' como 1 e 'Não' como 0
df[linguagem_cols] = df[linguagem_cols].applymap(lambda x: 1 if x == 'Sim' else 0 if x == 'Não' else pd.to_numeric(x, errors='coerce'))

# Criar DataFrame auxiliar
linguagens_df = df[linguagem_cols].sum().reset_index()
linguagens_df.columns = ['Linguagem', 'Número de Respondentes']

# Remover 'P21' do rótulo
linguagens_df['Linguagem'] = linguagens_df['Linguagem'].apply(lambda x: x.split('_')[-1].strip())

# Ordenar as linguagens por frequência de uso
linguagens_df = linguagens_df.sort_values(by='Número de Respondentes', ascending=False)

# Criar o gráfico de barras
plt.figure(figsize=(12, 8))
sns.barplot(x='Número de Respondentes', y='Linguagem', data=linguagens_df, palette='viridis')
plt.title('Frequência de Uso de Linguagens de Programação')
plt.xlabel('Número de Respondentes')
plt.ylabel('Linguagem de Programação')
plt.show()


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
df['Media de Salario'] = df['P2_h _Faixa salarial'].apply(extrair_media)
df = df[~df['P1_b _Genero'].isin(['Não Informado', 'Prefiro não informar'])]
# Agrupe os dados por gênero e calcule a média de salário para cada grupo
media_salario_por_genero = df.groupby('P1_b _Genero')['Media de Salario'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='P1_b _Genero', y='Media de Salario', data=media_salario_por_genero,hue='P1_b _Genero', palette='viridis')
plt.xlabel('Gênero')
plt.ylabel('Média de Salário')
plt.title('Média de Salário por Sexo')
plt.xticks(rotation=0)  # Mantém os rótulos do eixo x na posição padrão
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print(media_salario_por_genero)

cont_genero = df['P1_b _Genero'].value_counts()
print(cont_genero)
