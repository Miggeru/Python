numero = int(input("Insira seu valor e lhe direi se ele é negativo ou positivo: "))

if numero >= 0:
    print(f'O número {numero} é positivo')
elif numero < 0:
    print(f'O número {numero} é negativo')
else:
    print(f'Valor inválido')