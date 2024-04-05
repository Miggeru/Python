numero1 = int(input('Escreva um número: '))
numero2 = int(input('Escreva um número: '))

if numero1 > numero2:
    print(f'O número {numero1} é maior que o {numero2}')
elif numero1 < numero2:
    print(f'O número {numero2} é maior que o {numero1}')
elif numero1 == numero2:
    print(f'O número {numero1} é igual ao {numero2}')
else:
    print('Valor inválido')