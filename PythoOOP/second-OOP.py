#Trying to use input with OOP

import self

class Pessoa:

    def __init__(self):
        self.nome = input('Escreva seu nome: ')
        self.idade = input('Escreva sua idade: ')
        self.altura = input('Escreva sua altura: ')
        self.sexo = input('Escreva seu sexo: ')


    def mostrar_pessoa(self):
        print('-'*30)
        print(f'Seu nome é: {self.nome}')
        print('-'*30)
        print(f'Sua idade é: {self.idade}')
        print('-'*30)
        print(f'Sua altura é: {self.altura}')
        print('-'*30)
        print(f'Seu sexo é: {self.sexo}')
        print('-'*30)

pessoa1 = Pessoa()
pessoa1.mostrar_pessoa()