# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas)

quantidade_de_hora_trabalho = int(input('Digita a quantidade de horas que você trabalhou no mês anterior: '))
while quantidade_de_hora_trabalho < 0:
    print('A quantidade de horas não pode ser negativa. Por favor, digite um valor válido')
    quantidade_de_hora_trabalho = int(input('Digita a quantidade de horas que você trabalhou no mês anterior: '))

salario_por_hora = float(input("Digite seu salário por hora: R$ "))

horas_normais_mes = 160
if quantidade_de_hora_trabalho <= horas_normais_mes:
    salario_total = quantidade_de_hora_trabalho * salario_por_hora
    
else:
    hora_extra = quantidade_de_hora_trabalho - horas_normais_mes
    salario_total = (horas_normais_mes * salario_por_hora) + (hora_extra * salario_por_hora * 1.5)
print(f'Seu salário mensal do mês anterior é : R$ {salario_total:.2f}')