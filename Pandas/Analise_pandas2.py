import pandas as pd

# dt_promo = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Promocoes.csv', sep=';')
dt_produtos = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Cadastro Produtos.csv', sep=';')
dt_clientes = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Clientes.csv', sep=';')
dt_lojas = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Lojas.csv', sep=';')
dt_vendas2017 = pd.read_csv(r'E:\Programas\Projetos-Python\Pandas\Contoso - Vendas  - 2017.csv', sep=';')

# axis=0 for rows and axis=1 for columns 
dt_clientes = dt_clientes.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)


# print(dt_vendas2017)
print(dt_clientes)
# print(dt_produtos)

#### parei no tempo 34:16