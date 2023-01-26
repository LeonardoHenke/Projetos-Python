import mods
import time
import os



escolha_user = 1

while escolha_user != 0:
    os.system('cls')
    mods.painel_calculadora()
    escolha_user = int(input('Realizar a operação: '))
    if escolha_user == 1:
        mods.soma()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 2:
        mods.subtracao()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 3:
        mods.multiplicacao()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 4:
        mods.divisao()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 5:
        mods.exponencial()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 6:
        break
    else:
        print('Opção inválida, aguarde e tente novamente!')
        escolha_user = 1
        time.sleep(5)
