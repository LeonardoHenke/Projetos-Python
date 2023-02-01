user = -69
maior = 0

# Pegando os números
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

# Menu
while user != 5:
    print(f'''Os números escolhidos foram: {n1} e {n2}
---------------------
        Menu
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
---------------------''')
    user = int(input('O que deseja fazer? '))

# Resultado
    if user == 1:
        print(f'Resultado: {n1 + n2}')
    elif user == 2:
        print(f'Resultado: {n1 * n2}')
    elif user == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número é o: {maior}')
    elif user == 4:
        novo1 = int(input('Primeiro número: '))
        novo2 = int(input('Segundo número: '))
        n1 = novo1
        n2 = novo2
    else:
        print('Escolha inválida, tente novamente')
print('Saindo...')