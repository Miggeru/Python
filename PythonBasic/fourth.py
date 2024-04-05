#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

letra = input('Escreva uma letra e direi se é consoante ou vogal: ')

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra {letra} é uma vogal')
else:
    print('É consoante')