import pandas as pd

# fazendo a leitura das tabelas e atribuindo as variaveis
## dt_promo = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Promocoes.csv', sep=';')
df_produtos = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Cadastro Produtos.csv', sep=';')
df_clientes = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Clientes.csv', sep=';')
df_lojas = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Lojas.csv', sep=';')
df_vendas2017 = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Vendas  - 2017.csv', sep=';')


# tirar as colunas escolhidas como argumentos. Usando axis=0 para linhas and axis=1 for colunas 
## dt_clientes = dt_clientes.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)

# pegar apenas as colunas desejadas como argumento
coluna_desejada_clientes = ['ID Cliente', 'E-mail']
df_clientes = df_clientes[coluna_desejada_clientes]

coluna_desejada_produtos = ['ID Produto', 'Nome da Marca']
df_produtos = df_produtos[coluna_desejada_produtos]

coluna_desejada_lojas = ['ID Loja', 'Nome da Loja']
df_lojas = df_lojas[coluna_desejada_lojas]

# agrupar os dataframes desejados. Precisamos que o dataframe base tenha uma coluna que seja igual ao outro dataframe que sera adicionado, so assim ele vai identificar as informacoes certas nas linhas certas
df_vendas2017 = df_vendas2017.merge(df_produtos, on='ID Produto')
df_vendas2017 = df_vendas2017.merge(df_clientes, on='ID Cliente')
df_vendas2017 = df_vendas2017.merge(df_lojas, on='ID Loja')

# Alterar o nome de alguma coluna- dataframe.rename(columns={'nome da coluna' : 'novo nome'})   {}
df_vendas2017 = df_vendas2017.rename(columns={'E-mail' : 'E-mail do Cliente'})




print(df_vendas2017)
#print(dt_clientes[:4])
#print(df_produtos[:4])
#print(df_lojas[:4])






#### Video: 24 - Tempo: 34:16