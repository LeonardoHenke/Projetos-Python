import pandas as pd

# vai ler a tabela pelo caminho dado, atribuindo ela a uma variavel. Separando os dados em colunas pelo argumento ';'
tabela_vendas = pd.read_csv(r'E:\Programas\Projetos Python\Pandas\Contoso - Vendas  - 2017.csv', sep=';') 

# printar a tabela inteira
## print(tabela_vendas)

# printar apenas o argumento escolhido. No caso, todas as linhas da coluna 'ID Cliente'
## print(tabela_vendas['ID Cliente'])

# printar apenas o argumento escolhido. No caso, as informacoes ate a linha 3
## print(tabela_vendas[:3])

# printar apenas o argumento escolhido. No caso, as informacoes da coluna 'ID Cliente' ate a linha 3
## print(tabela_vendas['ID Cliente'][:3])

# printar as colulas escolhidas (dentro de []) e depois passando outro argumento para pegar apenas ate a 3 linha
## print(tabela_vendas[['ID Cliente', 'ID Canal']][:3])

# printa um item especifico nao da linha 3, mas da 4. 3 [e a quarta linha, pois comeca no 0
## print(tabela_vendas['ID Cliente'][3])

# printa as informacoes resumidas da tabela. Muito necessario caso a tabela tenha muitas colunas
## print(tabela_vendas.info())

# cria uma lista de clientes
## lista_clientes = tabela_vendas['ID Cliente']
## print(lista_clientes)

# criar uma lista de para controle de estoque
lista_colunas = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
print(tabela_vendas[lista_colunas])