def somar(x, y):
    resultado = x + y
    return resultado

def main():
    valorX = float(input('Digite o valor X: '))
    valorY = float(input('Digite o valor y: '))

    resultado_soma = somar(valorX, valorY)

    print(f'A soma de {valorY} e {valorX} é: {resultado_soma}')

if __name__ == '__main__':
    main()