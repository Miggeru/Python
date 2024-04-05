#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
#para o sindicato, faça um programa que nos dê:

 #   salário bruto.
  #  quanto pagou ao INSS.
   # quanto pagou ao sindicato.
    #o salário líquido.

salarioHora = float(input('Seu salário por hora: '))
horasTrabalhadas = float(input('Horas trabalhadas (jornada de trabalho): '))
diasTrabalhados = int(input('Quantos dias você trabalhou: '))

ganhoPorDia = salarioHora * horasTrabalhadas
ganhoMensal = ganhoPorDia * diasTrabalhados

print(f'Seu salário bruto é de: {ganhoMensal}')

ir = ganhoMensal - (ganhoMensal * 0.11)
inss = ir - (ir * 0.08)
sindicato = inss - (inss * 0.05)

pagoIr = ganhoMensal * 0.11
pagoINSS = pagoIr * 0.08
pagoSIN = pagoINSS * 0.05

print('Você pagou ao IR {:.2f}'.format(pagoIr))
print('Você pagou ao INSS {:.2f}'.format(pagoINSS))
print('Você pagou ao Sindicato {:.2f}'.format(pagoSIN))

salarioL = sindicato

print('Seu salário líquido é de: {:.2f}'.format(salarioL))