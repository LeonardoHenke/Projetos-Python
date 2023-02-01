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
        print()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 2:
        mods.subtracao()
        print()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 3:
        mods.multiplicacao()
        print()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 4:
        mods.divisao()
        print()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 5:
        mods.exponencial()
        print()
        escolha_user = int(input('Realizar a operação: '))
    elif escolha_user == 6:
        os.system('cls')
        break
    else:
        print('Opção inválida, aguarde e tente novamente!')
        escolha_user = 1
        time.sleep(5)
