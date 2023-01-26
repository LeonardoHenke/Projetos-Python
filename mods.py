import os


def titulo():
    print()
    print('='*29)
    print('Calculadora by Leonardo Henke')
    print('='*29)
    print()


def painel_calculadora():
    titulo()
    lista_painel = ['Soma', 'Subtração',
                    'Multiplicação', 'Divisão', 'Exponencial', 'Encerrar programa']
    print('-'*29)
    for num, escolha in enumerate(lista_painel):
        print(f'[{num + 1}] : [{escolha}]')
    print('-'*29)
    print()


def soma():
    os.system('cls')
    titulo()
    print('Você escolheu a opção [1] : Somar')
    print()
    num1 = float(input('Valor 1: '))
    num2 = float(input('Valor 2: '))
    print()
    print(f'{num1} + {num2} = {num1 + num2}')
    nova_operacao()


def subtracao():
    os.system('cls')
    titulo()
    print('Você escolheu a opção [2] : Subtração')
    print()
    num1 = float(input('Valor 1: '))
    num2 = float(input('Valor 2: '))
    print()
    print(f'{num1} - {num2} = {num1 - num2}')
    nova_operacao()


def multiplicacao():
    os.system('cls')
    titulo()
    print('Você escolheu a opção [3] : Multiplicação')
    print()
    num1 = float(input('Valor 1: '))
    num2 = float(input('Valor 2: '))
    print()
    print(f'{num1} x {num2} = {num1 * num2:.2f}')
    nova_operacao()


def divisao():
    os.system('cls')
    titulo()
    print('Você escolheu a opção [4] : Divisão')
    print()
    num1 = float(input('Valor 1: '))
    num2 = float(input('Valor 2: '))
    print()
    print(f'{num1} / {num2} = {num1 / num2:.3f}')
    nova_operacao()


def exponencial():
    os.system('cls')
    titulo()
    print('Você escolheu a opção [5] : Exponencial')
    print()
    num1 = float(input('Valor 1: '))
    num2 = float(input('Valor 2: '))
    print()
    print(f'{num1} ** {num2} = {num1 ** num2}')
    nova_operacao()


def nova_operacao():
    print()
    print('='*29)
    lista_segunda_escolha = ['Encerrar Programa', 'Voltar para o Menu']
    for num, escolha in enumerate(lista_segunda_escolha):
        print(f'[{num}] : [{escolha}]')
