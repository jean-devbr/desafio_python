# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input('Digite a idade em anos: '))
mes = int(input('Digite a idade em mês : '))
dias = int(input('Digite a idade em dias: '))

total = (anos * 365) + (mes * 30) + 30
print(f'Você tem total de dias {total}')