import self


class Produto: #Creating class 'Produto'

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Func to show the items
    def mostrar_info(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: R${self.preco}')
        print(f'Quantidade: {self.quantidade}')


#Data input to the attributes
p1 = Produto('Água', 1.99, 20)
p1.mostrar_info()
print('='*30)
p2 = Produto('Leite', 3.45, 15)
p2.mostrar_info()


####################


#Creating class 'Animal'
class Animal:

    def __init__(self, raca, idade, cor):
        self.raca = raca
        self.idade = idade
        self.cor = cor

    # Func to show the items
    def mostrar_carac(self):
        print(f'A raça do animal é: {self.raca}')
        print(f'A idade do animal é: {self.idade}')
        print(f'A cor do animal é: {self.cor}')


#Data input to the attributes
a1 = Animal('Gato', '4', 'Marrom')
print('='*30)
a1.mostrar_carac()


#Creating class 'AnimalMam' that Inherit class 'Animal'
class AnimalMam(Animal):

    def __init__(self, raca, idade, cor, tipo):
        super().__init__(raca, idade, cor)
        self.tipo = tipo

    #Show the new func 'tipo'
    def mostrar_tipo(self):
        print(f'O animal é do tipo: {self.tipo}')


p3 = AnimalMam('Cão', '9', 'Preto', 'Mamífero')
print('='*30)
p3.mostrar_carac()
p3.mostrar_tipo()
