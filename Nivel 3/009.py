#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário

salario_mensal = float(input('Digite qual é o seu salário: '))
reajuste = float(input('Qual foi o reajuste no seu salário em porcentagem (%): '))

valor_aumentado = (salario_mensal * reajuste) / 100
salario_novo = salario_mensal + valor_aumentado
print(f'Salário novo é : R$ {salario_novo:.2f}')