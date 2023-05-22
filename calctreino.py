'''
opcao = ''
a = 0
b = 0

while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    print('Selecione uma opção:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    opcao = input('Digite o número da operação desejada: ')

    if opcao == '1':
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        print('O resultado da soma é:', a + b)
    elif opcao == '2':
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        if a>b:
            print('O resultado da subtracao é:', a - b)
        else:
            print('O resultado da subtracao é:', b - a)
    if opcao =='3':
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        print('O resultado da multiplicacao e:', a * b )
    if opcao =='4':
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        print('O resultado da divisao e: ', a / b)
    if opcao > '5':
        print('Opcao invalida')
        exit
        '''

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError('Não é possível dividir por zero')
    return a / b

opcao = ''

while opcao not in ('1', '2', '3', '4'):
    print('Selecione uma opção:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    opcao = input('Digite o número da operação desejada: ')

    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))

    if opcao == '1':
        print('O resultado da soma é:', soma(a, b))
    elif opcao == '2':
        print('O resultado da subtração é:', subtracao(a, b))
    elif opcao == '3':
        print('O resultado da multiplicação é:', multiplicacao(a, b))
    elif opcao == '4':
        try:
            print('O resultado da divisão é:', divisao(a, b))
        except ValueError as e:
            print(e)
    else:
        print('Opção inválida')



        


    
