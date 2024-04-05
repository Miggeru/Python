#Faça um programa para a leitura de 3 notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:

 #   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  #  A mensagem "Reprovado", se a média for menor do que sete;
   # A mensagem "Aprovado com Distinção", se a média for igual a dez. 

print("Escreva 3 notas")
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

somaNotas = nota1 + nota2 + nota3
mediaNotas = somaNotas / 3

print('Sua média foi: ' + str(mediaNotas))
if mediaNotas < 7:
    print('Reprovado')
elif mediaNotas >= 7 and mediaNotas < 10:
    print('Aprovado')
elif mediaNotas == 10:
    print('Aprovado com distinção')
else:
    print('Valor inválido')